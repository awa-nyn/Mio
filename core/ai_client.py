from datetime import datetime, timedelta
import time
import uuid
from prompt_toolkit import PromptSession
from openai import OpenAI
from pathlib import Path
from openai import omit
import sys
import asyncio
from openai import APIError
import json
import platform
import sqlite3
from core.config import c

session = PromptSession(multiline=True)
# 获取路径
if getattr(sys, "frozen", False):
    source = Path(sys.executable).parent
else:
    source = Path(__file__).parent.parent

# 对话逻辑
def chat(client: OpenAI):
    asyncio.run(_chat(client))

async def _chat(client: OpenAI):
    from utils import file
    from core import time_
    from core import mem
    from tools import tool
    from core.commands import act
    from tools import manager

    # 检查历史记录是否需要更新

    c.exist(source / "memory" / "history.json")
    c.exist(source / "memory" / "token.json")
    with open(source / "memory" / "history.json", "r", encoding="utf-8") as f:
        history = json.load(f)
    total_tokens = 0
    if (source / "memory" / "token.json").stat().st_size != 0:
        with open(source / "memory" / "token.json", "r", encoding="utf-8") as f:
            total_tokens = json.load(f).get("total_tokens", 0)
    if not history:
        timestamp = history[0].get("content").get("text")
        timestamp = datetime.strptime(timestamp[1:9], "%y-%m-%d").date()
        keep = ((datetime.now() - timedelta(days=c.h_days))).date()
        # 是否超出天数
        if timestamp < keep:
            mem.update()
        # 是否超出token数
        elif total_tokens > c.h_tokens:
            mem.update()
            with open(source / "memory" / "token.json", "w", encoding="utf-8") as f:
                json.dump({"total_tokens": 0}, f, ensure_ascii=False, indent=4)

    # 检查图片数据文件大小，超过限制则更新历史记录
    c.exist(source / "memory" / "images_data.jsonl")
    with open(source / "memory" / "images_data.jsonl", "r", encoding="utf-8") as f:
        size = 0
        for line in f:
            if size == 0:
                first_id = json.loads(line).get("id")
            data = json.loads(line).get("size")
            if data:
                size += data
    if size > 47185920: # 45MB
        while True:
            mem.update()
            with open(source / "memory" / "images_data.jsonl", "r", encoding="utf-8") as f:
                while True:
                    line = f.readlines()
                    if line:
                        first_id_ = json.loads(line[0]).get("id")
                        break
            if first_id_ != first_id:
                break

    print("发送消息（Alt + Enter提交）:")

    while True:
        history_path = source / "memory" / "history.json"
        # 读取各文件内容
        if not history_path.exists():
            c.exist(history_path)
        if history_path.stat().st_size == 0:
            file.write(history_path, [], mode='w')
        history: list = file.read(history_path)

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
                            # base64
                            if images_list[0].get("image_url"):
                                if idx == 0:
                                    images_list = []
                                    print("已删除所有图片")
                                elif idx > len(images_list):
                                    print("没有这张图片")
                                    continue
                                else:
                                    del images_list[idx-1]
                                    print(f"已删除第{idx}张图片")
                            # Files API
                            elif images_list[0].get("file_id"):
                                if idx == 0:
                                    img = images_list[0].get("file_id")
                                    keep_data = []
                                    with open(source / "memory" / "images_data.jsonl", "r", encoding="utf-8") as f:
                                        for line in f:
                                            data = json.loads(line)
                                            if data.get("file_id") == img:
                                                break
                                            keep_data.append(data)
                                    if keep_data:
                                        with open(source / "memory" / "images_data.jsonl", "w", encoding="utf-8") as f:
                                            for data in keep_data:
                                                json.dump(data, f, ensure_ascii=False)
                                                f.write("\n")
                                    else:
                                        with open(source / "memory" / "images_data.jsonl", "w", encoding="utf-8") as f:
                                            f.write("")
                                    for image in images_list:
                                        client.files.delete(file_id=image.get("file_id"))
                                    images_list = []
                                    print("已删除所有图片")
                                elif idx > len(images_list):
                                    print("没有这张图片")
                                    continue
                                else:
                                    img = images_list[idx-1].get("file_id")
                                    keep_data = []
                                    with open(source / "memory" / "images_data.jsonl", "r", encoding="utf-8") as f:
                                        for line in f:
                                            data = json.loads(line)
                                            if data.get("file_id") == img:
                                                continue
                                            keep_data.append(data)
                                    if keep_data:
                                        with open(source / "memory" / "images_data.jsonl", "w", encoding="utf-8") as f:
                                            for data in keep_data:
                                                json.dump(data, f, ensure_ascii=False)
                                                f.write("\n")
                                    else:
                                        with open(source / "memory" / "images_data.jsonl", "w", encoding="utf-8") as f:
                                            f.write("")
                                    client.files.delete(file_id=img)
                                    del images_list[idx-1]
                                    print(f"已删除第{idx}张图片")

                            else:
                                print("没有上传任何图片")
                    # 撤销操作
                    if type(return_) == dict and return_.get("rv") is not None:
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
                            json.dump(his, f, ensure_ascii=False, indent=4)
                        history = file.read(history_path)

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
        
        user_history = {"role": "user",
                "content": [{"type": "text", "text": msg_info + input_msg},
                ]}
        for f in files:
            user_history["content"].append(f)

        # 获取各文件所在路径
        system_path = source / "system.md"

        
        msg = history

        # 获取提示信息
        tip = time_.awareness()
        user_msg = user_history
        user_msg["content"][0]["text"] = msg_info + tip + input_msg

        # 获取工具路径
        if getattr(sys, "frozen", False):
            path = Path(sys._MEIPASS)
        else:
            path = Path(__file__).parent.parent

        tools_path = path / "tools" / "tools.json"
        tools = file.read(tools_path)

        # 调取数据库
        db_path = source / "memory" / "memory.db"
        system_msg = []
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='specified_memory'")
            if cursor.fetchone():
                cursor.execute("SELECT memory FROM specified_memory")
                memories = cursor.fetchall()
                if memories:
                    memory = [mem[0] for mem in memories]
                    system_msg = [
                        {"role": "system", "content": "[Specified Memory]\n" + "\n".join(memory)}
                        ]

        if not system_path.exists():
            system_path.touch()
        system = file.read(system_path)
        # 构造消息
        system_msg.append({"role": "system", "content":f"Environment: {platform.system()}\n" + system})
        msg = system_msg + msg
        msg.append(user_msg)

        # 构造请求
        try:
            response = client.chat.completions.create(
                model=c.model,
                tools=tools if c.tool else omit,
                messages=msg,
                stream=True,
                reasoning_effort=c.reasoning_effort,
                extra_body=c.extra_body
            )
        except APIError as e:
            print(f"请求失败，可能是模型或其他配置问题，错误信息：{e}")
            continue

        # TTS
        if c.tts and not c.free:
            from TTS.voice import TTS
            session_id = str(uuid.uuid4())
            tts = TTS(section_id=session_id)
            await tts.start()


        # 流式请求
        print(f"\n{c.assistant} >>> ", end="")
        while True:
            content = []
            reasoning_content = []
            calls = {}
            finish_reason = None
            num = 0
            first_user_msg = True
            for chunk in response:
                chunk = chunk.model_dump()  # 将chunk转换为字典
                delta = chunk["choices"][0].get("delta", {})
                if delta.get("reasoning_content"):
                    if c.think_output:
                        if num == 0:
                            num =1
                            print("<think>", end="")
                        print(delta["reasoning_content"], end="")    # 思考
                    reasoning_content.append(delta["reasoning_content"])
                if delta.get("content"):
                    if num == 1:
                        num = 2
                        print("</think>\n")
                    content.append(delta["content"])    # 将内容添加到列表中
                    print(delta["content"], end="", flush=True)     # 流式输出
                    if c.tts and not c.free:
                        await tts.put_text(delta["content"])   # 将内容放入队列中
                    await asyncio.sleep(0.05)
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
                    # 更新总token数
                    total_tokens = (chunk.get("usage") or {}).get("total_tokens", 0)
                    if total_tokens:
                        c.exist(source / "memory" / "token.json")
                        with open(source / "memory" / "token.json", "w", encoding="utf-8") as f:
                            json.dump({"total_tokens": total_tokens}, f, ensure_ascii=False, indent=4)
                    print("\n")
                    resp = ''.join(content)
                    # 将用户输入写入历史记录
                    if first_user_msg:
                        history.append(user_msg)
                        first_user_msg = False
                    # 将助手输出写入历史记录
                    assistant_msg = {"role": "assistant", "content": resp}
                    # 将推理内容写入历史记录
                    if reasoning_content:
                        reasoning = ''.join(reasoning_content)
                        assistant_msg["reasoning_content"] = reasoning
                    history.append(assistant_msg)
                    # 将历史记录写入文件
                    with open(history_path, "w", encoding="utf-8") as f:
                        json.dump(history, f, ensure_ascii=False, indent=4)
                    if finish_reason == "length":
                        print("\n输出终止：单次输出字数达到上限（本次对话已记录）\n")
                    elif finish_reason == "content_filter":
                        print("\n输出终止：输出内容被过滤（本次对话已记录）\n")
                    # 工具调用
                    elif finish_reason ==  "tool_calls":
                        calls = dict(sorted(calls.items()))  # 排序
                        history.append(     # 返回工具调用请求
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
                            elif arg.get("content") and arg.get("num"):
                                if arg.get("time") and arg.get("role"):
                                    res = str(manager.search_memory(arg["content"], arg["num"], arg["time"], arg["role"]))
                                elif arg.get("time"):
                                    res = str(manager.search_memory(arg["content"], arg["num"], arg["time"]))
                                elif arg.get("role"):
                                    res = str(manager.search_memory(arg["content"], arg["num"], role=arg["role"]))
                                else:
                                    res = str(manager.search_memory(arg["content"], arg["num"]))
                            elif arg.get("memory_text"):
                                res = str(manager.specify_memory(arg["memory_text"]))
                            elif arg.get("query"):
                                if arg.get("top"):
                                    res = str(manager.online_search(arg["query"], arg["top"]))
                                else:
                                    res = str(manager.online_search(arg["query"]))
                            elif arg.get("command") and arg.get("content"):
                                res = str(manager.cmd(arg["command"], arg["content"]))
                            else:
                                res = "参数错误"
                            history.append(
                                {"role": "tool", "tool_call_id": call_id, "content": res}
                            )
                            # 记录工具调用
                            with open(history_path, "w", encoding="utf-8") as f:
                                json.dump(history, f, ensure_ascii=False, indent=4)

            if finish_reason != "tool_calls":
                if finish_reason is None:
                    if c.tts and not c.free:
                        await tts.put_text(0)
                    print("\n输出终止：原因未知，可能是网络问题（本次对话未记录）\n")
                if c.tts and not c.free:
                    await tts.put_text(1)
                break
            else:
                # 重新构造消息
                try:
                    msg = history
                    msg = system_msg + msg
                    # 返回工具调用结果
                    response = client.chat.completions.create(
                        model=c.model,
                        tools=tools,
                        messages=msg,
                        stream=True,
                        reasoning_effort=c.reasoning_effort,
                        extra_body=c.extra_body
                    )
                except APIError as e:
                    print(f"再次请求失败，错误信息：{e}")
                    break

        if c.tts and not c.free:
            await tts.finish()
