import json
from pathlib import Path
import sys
import asyncio
import aiohttp
import datetime
from core.config import c
from aiohttp import ClientConnectorError

if getattr(sys, "frozen", False):
    source = Path(sys._MEIPASS)
else:
    source = Path(__file__).parent.parent

path = source / "utils" /"Default Workflow.json"
with open(path, "r", encoding="utf-8") as f:
    default_workflow = json.load(f)



class workflow:
    def __init__(self):
        self.default_workflow = default_workflow
        self.timestamp = None
        self.upload = None
        self.success = None

    def default(self, args: dict):
        path = None
        # 将args中的参数替换到default_workflow中
        for key, value in args.items():
            match key:
                case "name":
                    path = c.comfyui_path / "user" / "default" / "workflows_api" / value
                    if not path.suffix or path.suffix != ".json":
                        return f"工作流名称 {value} 不合法，请检查名称是否包含后缀 .json"
                    if not path.exists():
                        if not path.parent.exists():
                            path.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            path.touch()
                        except OSError as e:
                            return f"文件名非法或系统层面创建失败：{e}"
                case "filename_prefix":
                    self.default_workflow["12"]["inputs"]["filename_prefix"] = value
                case "depth":
                    self.default_workflow["12"]["inputs"]["format.bit_depth"] = value
                case "width":
                    self.default_workflow["5"]["inputs"]["width"] = value
                case "height":
                    self.default_workflow["5"]["inputs"]["height"] = value
                case "zoom_scale":
                    self.default_workflow["8"]["inputs"]["upscale_method"] = value
                case "zoom":
                    self.default_workflow["8"]["inputs"]["scale_by"] = value
                case "positive":
                    self.default_workflow["2"]["inputs"]["text"] = value
                case "checkpoint":
                    model_path = c.comfyui_path / "models" / "checkpoints" / value
                    if not model_path.exists():
                        return f"模型文件 {value} 不存在，请检查路径是否正确"
                    self.default_workflow["1"]["inputs"]["ckpt_name"] = value
                case "negative":
                    self.default_workflow["3"]["inputs"]["text"] = value
                case "sampler":
                    self.default_workflow["6"]["inputs"]["sampler_name"] = value
                    self.default_workflow["9"]["inputs"]["sampler_name"] = value
                case "steps":
                    self.default_workflow["6"]["inputs"]["steps"] = value
                    self.default_workflow["9"]["inputs"]["steps"] = value
                case "scheduler":
                    self.default_workflow["6"]["inputs"]["scheduler"] = value
                    self.default_workflow["9"]["inputs"]["scheduler"] = value
                case "cfg1":
                    self.default_workflow["6"]["inputs"]["cfg"] = value
                case "cfg2":
                    self.default_workflow["9"]["inputs"]["cfg"] = value
                case "denoise":
                    self.default_workflow["9"]["inputs"]["denoise"] = value
                case _:
                    return f"参数 {key} 不存在，请检查参数名称是否正确"

        if path is None:
            return "未指定工作流名称，请检查参数中是否包含 name"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.default_workflow, f, ensure_ascii=False)
        return f"已生成默认工作流文件 {path}"

    @staticmethod
    async def confirm():
        if c.paint_confirm:
            inp = input(f"{c.assistant}请求调用ComfyUI进行绘画，是否同意？(y/n)")
            while True:
                if inp.lower() == "y":
                    return True
                elif inp.lower() == "n":
                    return False
        else:
            print(f"\n{c.assistant}正在调用ComfyUI进行绘画")
            return True

    async def paint(self, path: Path):
        address = f"http://127.0.0.1:{c.comfyui_port}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{address}/system_stats") as response:
                    if response.status != 200:
                        print(f"\n无法连接到ComfyUI，请确保ComfyUI已启动并运行在端口 {c.comfyui_port} 上")
                        self.success = False
                        return

                with open(path, "r", encoding="utf-8") as f:
                    workflow_data = json.load(f)
                async with session.post(f"{address}/prompt", json={"prompt": workflow_data}) as resp:
                    data = await resp.json()
                    data_id = data.get("prompt_id")
                    if not data_id:
                        print(f"\n绘画请求失败，错误信息：{data.get('error', '未知错误')}")
                        self.success = f"绘画请求失败，错误信息：{data.get('error', '未知错误')}"
                        return
                    self.success = True
                # 初始计时
                start_time = datetime.datetime.now()
                timeout = datetime.timedelta(seconds=300)  # 设置超时时间为300秒
                while True:
                    async with session.get(f"{address}/history/{data_id}") as resp:
                        result = await resp.json()
                        if data_id in result:
                            if result[data_id]["status"]["status_str"] == "success":
                                break
                            elif result[data_id]["status"]["status_str"] == "error":
                                print(f"\n绘画失败，原因未知，请检查ComfyUI日志")
                                return
                            elif result[data_id]["status"].get("error"):
                                print(f"\n绘画失败，原因：{result[data_id]['status']['error']}")
                                return
                    await asyncio.sleep(1)
                    # 超时判定
                    if datetime.datetime.now() - start_time > timeout:
                        print(f"\n绘画超时，请检查ComfyUI是否正常运行")
                        return
        except ClientConnectorError:
            print(f"\n无法连接到ComfyUI，请确保ComfyUI已启动并运行在端口 {c.comfyui_port} 上")
            self.success = False
            return

        default_output_path = c.comfyui_path / "output"
        outputs_id = []
        for k, v in workflow_data.items():
            if v["class_type"] == "SaveImage" or v["type"] == "SaveImageAdvanced":
                outputs_id.append(k)
                break

        images_info = []
        for output_id in outputs_id:
            images_info.append(result[data_id]["outputs"][str(output_id)]["images"])
        files_path = []
        if c.output_path:
            output_path = Path(c.output_path)
            if not output_path.exists():
                output_path.mkdir(parents=True, exist_ok=True)
            import shutil
            try:
                for item in images_info:
                    for image_info in item:
                        filename = image_info["filename"]
                        default_path = default_output_path
                        if image_info.get("subfolder"):
                            default_path = default_path / image_info["subfolder"]
                        file_path = default_path / filename
                        shutil.move(file_path, output_path)
                        files_path.append(str(output_path / filename))
            except Exception as e:
                for item in images_info:
                    for image_info in item:
                        filename = image_info["filename"]
                        default_path = default_output_path
                        if image_info.get("subfolder"):
                            default_path = default_path / image_info["subfolder"]
                        file_path = default_path / filename
                        if file_path.exists():
                            file_path.unlink()
                print(f"\n将图片保存到指定目录失败：{e}")
                return
        else:
            for item in images_info:
                for image_info in item:
                    filename = image_info["filename"]
                    default_path = default_output_path
                    if image_info.get("subfolder"):
                        default_path = default_path / image_info["subfolder"]
                    files_path.append(str(default_path / filename))

        print(f"\n绘画完成，图片已保存到以下路径：")
        print("\t"+"\t\n".join(files_path))

        from core import images
        from core import time_
        self.timestamp = f"[{time_.get()}]"
        self.upload = images.upload_images(files_path)
        