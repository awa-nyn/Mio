import sys
from pathlib import Path
from datetime import datetime, timedelta
import json
import uuid
import chromadb
from core.config import c
import json

if getattr(sys, "frozen", False):
    source = Path(sys.executable).parent
else:
    source = Path(__file__).parent.parent

def update():
    from utils import file
    from main import client_get
    # 历史记录
    history_path = source / "memory" / "history.json"
    c.exist(history_path)
    if history_path.stat().st_size == 0:
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    # 记忆库
    memory_path = source / "memory" / "memory"
    # 图片记录
    images_data_path = source / "memory" / "images_data.jsonl"
    if not images_data_path.exists():
        images_data_path.touch()
    if images_data_path.stat().st_size == 0 and c.files_api:
        client = client_get()
        files = client.files.list(order="desc")
        for f in files.data:
            client.files.delete(f.id)
        
    # 如果向量库名称被文件占用
    if memory_path.exists() and memory_path.is_file():
        memory_path.unlink()

    # 连接向量库
    client_db = chromadb.PersistentClient(path=str(memory_path))
    collection = client_db.get_or_create_collection("memories")
    history: list = file.read(history_path)
    time_needness = (datetime.now() - timedelta(days=c.h_days)).date()
    first_timestamp = datetime.strptime(history[0]["content"][0]["text"][1:9], "%y-%m-%d")
    while True:
        if not history:
            break
        timestamp = None
        while True:
            role = history[0]["role"]
            # 将用户消息存入向量库
            if role == "user":
                timestamp = history[0]["content"][0]["text"][1:9]
                collection.add(
                    ids=[str(uuid.uuid4())],
                    documents=[history[0]["content"][0]["text"]],
                    metadatas=[
                        {"year": int("20" + timestamp[0:2]),
                         "timestamp": timestamp,
                         "source": "user"}
                    ]
                )
                # 删除图片数据(base64)
                if history[0]["content"][0]["text"][21:27] == "[上传图片：":
                    import re
                    images = re.match(r"(.*?)]", history[0]["content"][0]["text"][27:]).group(1)
                    image = images.split("/")
                    for image_id in image:
                        data_list = []
                        keep = False
                        with open(images_data_path, "r", encoding="utf-8") as f:
                            for line in f:
                                line = line.strip()
                                if not line:
                                    continue
                                data = json.loads(line)
                                if data["id"] == image_id:
                                    keep = True
                                    continue
                                if keep:
                                    data_list.append(data)
                        if data_list:
                            with open(images_data_path, "w", encoding="utf-8") as f:
                                for data in data_list:
                                    json.dump(data, f, ensure_ascii=False)
                                    f.write("\n")
                # (Files API)
                elif len(history[0]["content"]) > 1 and history[0]["content"][1].get("file_id"):
                    for msg in history[0]["content"][1:]:
                        if msg.get("file_id"):
                            data_list = []
                            delete = []
                            keep = False
                            with open(images_data_path, "r", encoding="utf-8") as f:
                                for line in f:
                                    line = line.strip()
                                    if not line:
                                        continue
                                    data = json.loads(line)
                                    if not keep:
                                        delete.append(data["file_id"])
                                    if data["file_id"] == msg["file_id"]:
                                        keep = True
                                        continue
                                    if keep:
                                        data_list.append(data)
                            if data_list:
                                client = client_get()
                                with open(images_data_path, "w", encoding="utf-8") as f:
                                    for data in data_list:
                                        json.dump(data, f, ensure_ascii=False)
                                        f.write("\n")
                                    for file_id in delete:
                                        client.files.delete(file_id=file_id)

            # 将助手消息存入向量库
            elif role == "assistant" and history[0]["content"] is not None:
                collection.add(
                    ids=[str(uuid.uuid4())],
                    documents=[history[0]["content"]],
                    metadatas=[
                        {"year": int("20" + timestamp[0:2]),
                         "timestamp": timestamp,
                         "source": "assistant"}
                    ]
                )
            # 删除历史记录
            del history[0]
            if not history or history[0]["role"] == "user":
                break

        if not history:
            break
        timestamp = datetime.strptime(history[0]["content"][0]["text"][1:9], "%y-%m-%d")
        # 至少清理一天
        if timestamp.date() == first_timestamp.date():
            continue
        # 如果时间戳大于所需时间，则停止循环
        if timestamp.date() > time_needness:
            break

    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)