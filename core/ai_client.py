import time
from prompt_toolkit import PromptSession
from openai import OpenAI
from pathlib import Path
from openai import omit
import sys
import json
import platform
from utils import file
from core.config import c
from core import time_
from memory import mem
from tools import tool
from core import images
from commands import act

session = PromptSession(multiline=True)

# 对话逻辑
def chat(client: OpenAI):
    print("发送消息（Alt + Enter提交）:")

    while True:
        # 获取路径
        if getattr(sys, "frozen", False):
            source = Path(sys.executable).parent
        else:
            source = Path(__file__).parent.parent
        # 输入逻辑
        images_list = []
        while True:
            input_msg = session.prompt(f"{c.user} >>> ")
            return_ = act(input_msg)
            if return_:
                if c.upload_images:
                    # 上传图片
                    if type(return_) == list:
                        images_list.extend(return_)
                    elif type(return_) == dict:
                        # 删除图片
                        if return_.get("di") is not None:
                            idx = return_["di"]
                            if idx == 0:
                                images_list = []
                            elif idx < 0 or idx > len(images_list):
                                print("没有这张图片")
                                continue
                            else:
                                del images_list[idx-1]
                                print(f"已删除第{idx}张图片")
                # 撤销操作
                elif type(return_) == dict and return_.get("rv") is not None:
                    idx = return_["rv"]
                    with open(source / "memory" / "history.json", "r", encoding="utf-8") as f:
                        his = json.load(f)
                    for i in range(idx):
                        if his:
                            while True:
                                last = his.pop()
                                if last.get("role") == "user":
                                    break
                            if i == idx - 1:
                                print(f"已撤销最近{idx}轮记录")
                        else:
                            print(f"没有那么多历史记录可以撤销，仅撤销了最近的{i}轮记录")
                            break
                    with open(source / "memory" / "history.json", "w", encoding="utf-8") as f:
                        json.dump(his, f, ensure_ascii=False)

                else:
                    break
            elif return_ is None:
                break

        # 构造用户消息
        files = []
        msg_info = f"[{time_.get()}]"
        image_ids = []
        if images_list:
            for image in images_list:
                image: dict
                if image.get("file_id"):
                    files.append(image)
                else:
                    image_ids.append(image["id"])
                    image.pop("id")
                    files.append(image)

        if image_ids:
            msg_info += "[上传图片："
            msg_info += "/".join(image_ids)
            msg_info += "]"
        
        user_msg = {"role": "user",
                "content": [{"type": "text", "text": msg_info},
                ]}
        for file in files:
            user_msg["content"].append(file)
        

        # 获取各文件所在路径
        history_path = source / "memory" / "history.json"

        # 读取各文件内容
        history = file.read(history_path)

        # 记录时间戳
        timestamp = time_.get()
        
        tip = time_.awareness() # 获取提示信息

    
    
        
        if getattr(sys, "frozen", False):
            path = Path(sys._MEIPASS)
        else:
            path = Path(__file__).parent.parent

        tools_path = path / "tools" / "tools.json"
        tools = file.read(tools_path)

        response = client.chat.completions.create(
            model=config.get("model"),
            tools=tools if config.get("tool") else omit,
            messages=msg,
            stream=True,
            reasoning_effort=config.get("reasoning_effort"),
            extra_body=config.get("extra_body")
        )
        
        
        print(f"\n{config.get("assistant_name")} >>> ", end="")
        while True:
            content = []
            calls = {}
            finish_reason = None
            num = 0
            for chunk in response:
                chunk = chunk.model_dump()  # 将chunk转换为字典
                # print("DEBUG: ", chunk)
                delta = chunk["choices"][0].get("delta", {})
                if delta.get("reasoning"):
                    if num == 0:
                        num =1
                        print("<think>", end="")
                    print(delta["reasoning"], end="")    # 思考
                if delta.get("content"):
                    if num == 1:
                        num = 2
                        print("</think>\n")
                        print(f"{config.get("assistant_name")} >>> ", end="")
                    content.append(delta["content"])    # 将内容添加到列表中
                    print(delta["content"], end="", flush=True)     # 流式输出
                    time.sleep(0.05)
                if delta.get("tool_calls"):     # 如果存在工具调用
                    tool_calls = delta["tool_calls"]
                    for item in tool_calls:     # 遍历工具调用列表
                        idx = item["index"]     # 键为index参数
                        if not calls.get(idx):   # 如果尚未记录此工具调用请求
                            calls[idx] = {}
                        if item.get("id"):      # 记录id
                            calls[idx]["id"] = item["id"]
                        if item.get("function"):
                            if not calls[idx].get("function"):
                                calls[idx]["function"] = {}
                            if item["function"].get("name"):    # 记录调用工具名称
                                calls[idx]["function"]["name"] = item["function"]["name"]
                                

                            # 记录调用工具参数
                            if item["function"].get("arguments"):
                                if not calls[idx]["function"].get("arguments"):
                                    calls[idx]["function"]["arguments"] = ""
                                calls[idx]["function"]["arguments"] += item["function"]["arguments"]
            

                finish_reason = chunk["choices"][0].get("finish_reason")
                if finish_reason:
                    print("\n")
                    resp = ''.join(content)
                    file.write(history_path, user, mode='a')  # 将用户输入写入历史记录
                    system = {"identity": config.get("assistant_name"), "time": timestamp ,"content": resp}
                    file.write(history_path, system, mode='a')
                    if finish_reason == "length":
                        print("\n输出终止：单次输出字数达到上限（本次对话已记录）\n")
                    elif finish_reason == "content_filter":
                        print("\n输出终止：输出内容被过滤（本次对话已记录）\n")
                    # 工具调用
                    elif finish_reason ==  "tool_calls":
                        calls = dict(sorted(calls.items()))  # 排序
                        history = file.read(history_path)
                        msg = message(memory, history)
                        msg.append(     # 返回工具调用请求
                            {"role": "assistant", "content": None, "tool_calls": [
                                {
                                    "id": call["id"],
                                    "type": "function",
                                    "function": call["function"]
                                }for call in calls.values()
                            ]
                            }
                        )
                        # 构筑工具调用结果
                        for call in calls.values():
                            name = call["function"]["name"]
                            call_id = call["id"]
                            arg = json.loads(call["function"]["arguments"])
                            print(f"\n正在调用：{name}，参数：{arg}")      # 调用
                            # 调用工具
                            if arg.get("path") and (arg.get("content") is not None):
                                res = str(tool.io(name, arg["path"], arg["content"]))
                            elif arg.get("source") and arg.get("dest"):
                                res = str(tool.io(name, arg["source"], arg["dest"]))
                            elif arg.get("path") and arg.get("keyword"):
                                res = str(tool.io(name, arg["path"], arg["keyword"])) if not arg.get("type") \
                                    else str(tool.io(name, arg["path"], arg["keyword"], arg["type"]))
                            elif arg.get("path") and (arg.get("end") or arg.get("end") == 0):
                                res = str(tool.io(name, arg["path"], arg["end"])) if arg.get("start") is None \
                                    else str(tool.io(name, arg["path"], arg["end"], arg["start"]))
                            elif arg.get("path"):
                                res = str(tool.io(name, arg["path"]))
                            else:
                                res = "参数错误"
                            msg.append(
                                {"role": "tool", "tool_call_id": call_id, "content": res}
                            )
                            # 记录工具调用
                            tool_call = {"identity": config.get("assistant_name") + "(tool_call)", "time": timestamp , \
                                            "content": f"调用工具：{name}；参数：{str(arg)}；结果：{res}"}
                            file.write(history_path, tool_call, mode='a')
                        # 返回工具调用结果
                        response = client.chat.completions.create(
                            model=config.get("model"),
                            tools=tools,
                            messages=msg,
                            stream=True,
                            reasoning_effort=config.get("reasoning_effort"),
                            extra_body=config.get("extra_body")
                        )


            if finish_reason != "tool_calls":
                if finish_reason is None:
                    print("\n输出终止：原因未知，可能是网络问题（本次对话未记录）\n")
                break
 
def message(memory, history):
    # 获取提示词所在路径
    if getattr(sys, "frozen", False):
        source = Path(sys.executable).parent
    else:
        source = Path(__file__).parent.parent
        
    system_prompt = source / "system.md"
    
    environ = platform.system()
    if not system_prompt.exists():
        if not system_prompt.parent.exists():
            system_prompt.parent.mkdir(parents=True)
        system_prompt.touch()
    system_prompt = file.read(system_prompt)
    msg =   [
                {"role": "system", "content": "[Long-term Memory]\n" + memory},
                {"role": "system", "content": f"[Environment: {environ}]" + system_prompt},
                {"role": "assistant", "content": "[Conversation History]\n" + history},
            ]

    # 获取图片记忆
    if config.get("image_memory"):
            images_memory_path = source / "memory" / "images_memory.json"
            with open(images_memory_path, "r", encoding="utf-8") as f:
                msg += json.load(f)

    return msg