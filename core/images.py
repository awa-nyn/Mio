from tkinter import filedialog
from tkinter import Tk
from openai import APIError
from pathlib import Path
import sys
import magic
from PIL import Image
from core.config import c
from utils import file

def _select_files():
    root = Tk()
    root.withdraw() # 隐藏主窗口
    root.geometry('800x600') # 设置窗口大小
    path = filedialog.askopenfilenames(title="选择图片",
                                   filetypes=[("图片文件", "*.png *.jpg *.jpeg *.gif *.webp")]) # 打开文件选择对话框
    root.destroy() # 销毁主窗口
    return list(path)

def _mime(path):
    return magic.from_file(path, mime=True)

def upload_images():
    images_list = _select_files()
    if not images_list:
        print("未选择图片。")
        return None
    uploads = []

    if getattr(sys, "frozen", False):
        source = Path(sys.executable).parent
    else:
        source = Path(__file__).parent.parent

    images_data = source / "memory" / "images_data.jsonl"
    c.exist(images_data)

    
    if not c.files_api:
        import base64
        print("正在上传...\n")
        # 创建临时目录
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            n = 0
            for image in images_list:
                # 判断是否为图片
                if _mime(image)[:5] != "image":
                    print(f"{image}上传失败，原因：非图片，该文件真实类型：{_mime(image)}")
                    continue
                # 压缩图片尺寸
                img = Image.open(image)
                img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                tmp_path = Path(tmpdir) / f"{Path(image).name}"
                if _mime(image) == "image/png":
                    tmp_path = tmp_path.with_suffix(".webp")
                    img.save(tmp_path, format="WebP", quality=80)
                elif _mime(image) == "image/gif":
                    tmp_path = tmp_path.with_suffix(".jpeg")
                    img.save(tmp_path, format="JPEG", quality=80)
                else:
                    tmp_path = tmp_path.with_suffix(f".{_mime(image).split('/')[-1]}")
                    img.save(tmp_path, quality=80)

                # 转换为base64
                with open(tmp_path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                    eql = b64.count("=")
                    # 记录
                    size = (len(b64) - eql) * 3 // 4
                    import uuid
                    image_id = str(uuid.uuid4())
                    data = {"id": image_id, "size": size}
                    file.write(images_data, data)
                    n += 1
                    uploads.append({"type": "image_url", "image_url": {"url": f"data:{_mime(tmp_path)};base64,{b64}"}, "id": image_id})

        if len(uploads) == len(images_list):
            print("上传成功！\n")
        elif len(uploads) > 0:
            print("部分内容上传成功...\n")
        else:
            print("上传失败，请重试\n")
            return None
        return uploads

    
    from main import client_get
    client = client_get()

    print("正在上传...\n")
    for image in images_list:
        if Path(image).stat().st_size / 1024 / 1024 > 64:
            return "size"
        with open(image, "rb") as f:
            try:
                upload = client.files.create(file=f,
                                            purpose="user_data",
                                            expires_after={
                                                "anchor": "created_at",
                                                "seconds": 2592000
                                            })
            except APIError as a:
                raise APIError("上传失败！模型可能不支持OpenAI SDK的Files API。请修改相关配置项。错误信息：" + str(a))
        file.write(images_data, {"file_id": upload.id})
        uploads.append({"type": "file", "file_id": upload.id})


    print("上传成功！\n")
    return uploads

