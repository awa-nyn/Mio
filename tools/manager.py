from pathlib import Path
import sys
from typing import Self
import shutil
import sqlite3
import chromadb
from utils import file
from core.config import c
import platform
from utils import docx

class ToolManager:

    def __init__(self, *args):
        if len(args) == 1:
            self.path = Path(args[0])
        elif len(args) == 2:
            self.source = Path(args[0])
            self.dest = Path(args[1])

    def confirm(s, needness=False, two_path=False):
        def warpper(func):
            def apply(self: Self, *args, n=0, **kwargs):
                if opt(self, needness=needness, two_path=two_path):
                    try:
                        return func(self, *args, **kwargs)
                    except PermissionError:
                        if opt(self, permission=True):
                            if platform.system() == "Linux":
                                try:
                                    if two_path:
                                        self.source.chmod(0o644)
                                        self.dest.chmod(0o644)
                                    else:
                                        self.path.chmod(0o644)
                                    return func(self, *args, **kwargs)
                                except PermissionError:
                                    print("变更失败：你不是文件所有者。尝试联系文件所有者，或以sudo命令运行。")
                                    return s + "失败，权限不足"
                            else:
                                if n < 5:
                                    return apply(*args, n+1, **kwargs)
                                else:
                                    print("重试次数达到上限，重试失败。")
                                    return s + "失败，权限不足"
                        else:
                            return s + "失败，权限不足"
                    except FileNotFoundError:
                        return s + "失败，文件或路径不存在"
                    except NotADirectoryError:
                        return s + "失败，不是目录"
                    except IsADirectoryError:
                        return s + "失败，不是文件"
                    except FileExistsError:
                        return s + "失败，已存在同名文件或目录"
                    except Exception as e:
                        return s + "失败，原因：" + str(e)
                else:
                    return c.user + "拒绝了你的请求"

            def opt(self: Self, permission=False, needness=False, two_path=False):
                    if two_path:
                        tip = "将" + str(self.source) + s + str(self.dest)
                    else:
                        tip = s + str(self.path)
                    while True:
                        if permission:
                            if platform.system() == "Linux":
                                print("\n" + c.assistant + f"尝试{tip}，失败，原因：权限不足。尝试变更权限？（y/n）")
                            else:
                                print("\n" + c.assistant + f"尝试{tip}，失败，原因：权限不足。检查文件是否被占用，或尝试以管理员身份运行。重试？（y/n）")
                        elif needness:
                            print("\n" + c.assistant + f"请求{tip}，是否同意?（y/n）")
                        elif two_path:
                            print("\n" + c.assistant + f"请求{tip}，是否同意?（y/n）")
                        else:
                            return True
                        ans = input()
                        if ans == "y" or ans == "Y":
                            return True
                        elif ans == "n" or ans == "N":
                            return False

            return apply
        return warpper
        
    @confirm("访问")
    def _ls(self, path: Path):
        return sorted(path.iterdir(), key=lambda x:(not x.is_dir(), x.name))

    def lsr(self):
        p: Path = self.path
        if c.lsr:
            while True:
                print(f"{c.assistant}请求递归查看此目录下的所有文件列表：{str(p)}\n是否同意？（y/n）")
                confirm = input()
                if confirm == "y" or confirm == "Y":
                    return self._lsr(p)
                elif confirm == "n" or confirm == "N":
                    return c.user + "拒绝了你的请求"
        else:
            print(f"正在递归查看目录：{str(p)}")

    
    def _lsr(self, p, msg=None, i=-1, last=False):
        # 初始化
        if msg is None:
            msg = str(p) + "/\n"
        # 排序
        ls = self._ls(p)
        if ls == "访问失败，权限不足":
            return msg.rstrip('\n') + "：权限不足\n"
        elif ls == "访问失败，文件或路径不存在":
            return msg.rstrip('\n') + "：路径不存在\n"
        elif ls == "访问失败，不是目录":
            return msg.rstrip('\n') + "：这不是一个目录\n"
        elif not ls:  # 如果为空
            return msg.rstrip('\n') + "：空文件夹\n"
        
        for idx, item in enumerate(ls):
                if idx == len(ls) - 1:  # 如果是最后一个文件
                    if not last:    # 如果不在根目录最后一个文件夹内
                        b = True
                        if i != -1: # 递归运行
                            msg += "│  "
                            for _ in range(i):
                                msg += "│  "
                            b = False
                        msg += f"└────{item.name}"

                        if item.is_dir():   # 如果是文件夹
                            msg += "/\n"
                            return self._lsr(item, msg, i+1, b)
                        else:   # 如果是文件
                            return msg + "\n"
                    else:   # 如果是在根目录最后一个文件夹内
                        if i != -1: # 递归运行
                            msg += "   "
                            for _ in range(i):
                                msg += "   "
                        msg += f"└────{item.name}"
                        if item.is_dir():
                            msg += "/\n"
                            return self._lsr(item, msg, i+1, last)
                        else:
                            return msg + "\n"
                else:   # 如果不是最后一个文件
                    if not last:
                        if i != -1:
                            msg += "│  "
                            for _ in range(i):
                                msg += "│  "
                        msg += f"├────{item.name}"
                        if item.is_dir():
                            msg += "/\n"
                            msg = self._lsr(item, msg, i+1)
                        else:
                            msg += "\n"
                    else:
                        if i != -1:
                            msg += "   "
                            for _ in range(i):
                                msg += "│  "
                        msg += f"├────{item.name}"
                        if item.is_dir():
                            msg += "/\n"
                            msg = self._lsr(item, msg, i+1)
                        else:
                            msg += "\n"

    def ls(self):
        p: Path =self.path
        print(f"正在查看目录：{str(p)}")
        msg = str(p) + "/:\n"
        ls = self._ls(p)
        if ls == "访问失败，权限不足":
            return msg.rstrip('\n') + "：权限不足\n"
        elif ls == "访问失败，文件或路径不存在":
            return msg.rstrip('\n') + "：路径不存在\n"
        elif ls == "访问失败，不是目录":
            return msg.rstrip('\n') + "：这不是一个目录\n"
        elif not ls:
            return msg.strip('\n') + "空文件夹\n"
        
        for item in ls:
            if item.is_dir():
                msg += f"{item.name}/\n"
            else:
                msg += f"{item.name}\n"

        return msg

    @confirm("读取", needness = c.read)
    def read(self):
        p: Path = self.path
        if not c.read:
            print(f"正在读取文件：{str(p)}")
        return str(file.read(p))

    @confirm("读取", needness = c.read)
    def readl(self, end, start=1):
        if start < 1:
            start = 1
        p = self.path
        if not c.read:
            print(f"正在读取文件：{str(p)}，从第{start}行到第{end}行")
        content = []
        with open(p, 'r') as f:
            for i, line in enumerate(f, start=1):
                if i > end:
                    break
                if i >= start:
                    content.append(line)
        return '\n'.join(content)

    @confirm("写入", needness = c.write_a)
    def write_a(self, content):
        p: Path = self.path
        if not c.write_a:
            print(f"正在写入文件：{str(p)}")
        file.write(p, content)
        return "写入成功"

    @confirm("修改", needness = c.write_w)
    def write_w(self, content):
        p: Path = self.path
        if not c.write_w:
            print(f"正在修改文件：{str(p)}")
        file.write(p, content, 'w')
        return "修改成功"

    @confirm("创建", needness = c.create)
    def create_d(self):
        p: Path = self.path
        if not c.create:
            print(f"正在创建目录：{str(p)}")
        p.mkdir(parents=True, exist_ok=True)
        return "创建成功"

    @confirm("创建", needness = c.create)
    def create_f(self):
        p: Path = self.path
        if not c.create:
            print(f"正在创建文件：{str(p)}")
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
        p.touch(exist_ok=True)
        return "创建成功"

    @confirm("删除", needness = True)
    def delete(self):
        return self._del()
    
    def _del(self, path: Path=None, rtn=""):
        if path is None:    # 初始化
            path: Path = self.path
            msg = self.path.name
        elif path != self.path:
            msg = self.path.name + '/' + str(path.relative_to(self.path))
        
        if path.is_file():
            path.unlink()
            return rtn + msg + " 已删除\n"
        ls = self._ls(path)
        if ls == "访问失败，权限不足":
            return rtn + msg + "/ 删除失败：权限不足\n"
        elif ls == "访问失败，文件或路径不存在":
            return rtn + msg + "/ 删除失败：路径不存在\n"
        elif not ls:
            path.rmdir()
            return rtn + msg + "/ 已删除\n"

        for item in ls:
            if item.is_dir():
                if self._ls(item):
                    rtn = self._del(item, rtn)
                item.rmdir()
                rtn += f"{msg}/{item.name}/ 已删除\n"
            else:
                item.unlink()
                rtn += f"{msg}/{item.name} 已删除\n"

        if path == self.path:
            path.rmdir()
            rtn += f"{msg}/ 已删除"

        return rtn

    @confirm("移动", two_path = c.move)
    def move(self):
        src = self.source
        dst = self.dest
        if not c.move:
            print(f"正在移动：{str(src)} 到 {str(dst)}")
        if not dst.exists():
            dst.mkdir(parents=True, exist_ok=True)
        elif src.is_dir() and dst.is_file():
            return "不能把目录移动到文件上"
        elif dst.is_dir():
            conf = dst / src.name
            if conf.exists():
                return "目标路径已存在同名文件或目录，请删除后重试"
        shutil.move(src, dst)
        return "移动成功"

    @confirm(s = "复制", two_path = c.copy)
    def copy(self):
        src = self.source
        dst = self.dest
        if not c.copy:
            print(f"正在复制：{str(src)} 到 {str(dst)}")
        if not dst.exists():
            dst.mkdir(parents=True, exist_ok=True)
        elif src.is_dir() and dst.is_file():
            return "不能把目录复制到文件上"

        if src.is_file():
            conf = dst / src.name
            if dst.is_dir() and conf.exists() and conf.is_dir():
                return "目标路径已存在同名目录，请删除后重试"
            shutil.copy2(src, dst)
            return "复制成功"
        else:
            conf = dst / src.name
            if conf.exists() and conf.is_file():
                return "目标路径已存在同名文件，请删除后重试"
            dst = dst / src.name
            shutil.copytree(src, dst, dirs_exist_ok=True)
            return "复制成功"

    @confirm("重命名", needness = c.rename)
    def rename(self, name):
        p = self.path
        if not c.rename:
            print(f"正在重命名：{str(p)} 为 {name}")
        p.rename(p.parent / name)
        return "重命名成功"

    @confirm("获取信息", needness = c.info)
    def info(self):
        p = self.path
        if not c.info:
            print(f"正在获取文件信息：{str(p)}")
        return str(p.stat())

    @confirm("搜索")
    def search(self, keyword, type_=""):
        p = self.path
        if not c.search:
            if type_ == "file":
                print(f"正在搜索：{str(p)} 下的文件，关键字：{keyword}")
            elif type_ == "dir":
                print(f"正在搜索：{str(p)} 下的目录，关键字：{keyword}")
            else:
                print(f"正在搜索：{str(p)}下的内容，关键字：{keyword}")
        ls = []
        for item in p.rglob(keyword):
            files = str(item.relative_to(p))
            if not type_:
                ls.append(files) if item.is_file() else ls.append(files + "/")
            elif type_ == "file" and item.is_file():
                ls.append(files)
            elif type_ == "dir" and item.is_dir():
                ls.append(files + "/")

        return '\n'.join(ls)

    @confirm("读取", needness = c.read)
    def read_docx(self):
        p: Path = self.path
        if not c.read:
            print(f"正在读取文件：{str(p)}")
        return str(docx.docx_to_md(p))

    @confirm("写入", needness = c.overwrite_docx)
    def write_docx(self, content):
        p: Path = self.path
        if not c.overwrite_docx:
            print(f"正在写入docx文件：{str(p)}")
        return str(docx.md_to_docx(p, content))


def specify_memory(memory_text):
    # 连接数据库
    if getattr(sys, "frozen", False):
        source = Path(sys.executable).parent
    else:
        source = Path(__file__).parent.parent
    db_path = source / "memory" / "memory.db"
    c.exist(db_path)
    print(f"正在指定记忆：{memory_text}")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS specified_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                memory TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_DATE
                )
            '''
            )
        cursor.execute("INSERT INTO specified_memory (memory) VALUES (?)", (memory_text,))
    return f"已指定记忆：{memory_text}"

def search_memory(content, num, time=None, role=None):
    # 连接数据库
    if getattr(sys, "frozen", False):
        source = Path(sys.executable).parent
    else:
        source = Path(__file__).parent.parent
    memory_path = source / "memory" / "memory"
    client = chromadb.PersistentClient(path=str(memory_path))
    collection = client.get_or_create_collection("memories")
    result = collection.get(limit=1)
    if not result['ids']:
        return "目前没有任何记忆。"
    if time:
        result = collection.query(
            query_texts=[content],
            n_results=collection.count(),
            where={"source": role} if role else None,
            include=["documents", "metadatas"]
        )
        docs = [d for d, m in zip(result["documents"][0], result["metadatas"][0])
                if str(m.get("timestamp", "")).startswith(time)][:num]
        if not docs:
            return "未找到相关记忆。"
        return "\n".join(docs)
    elif role:
        result = collection.query(
            query_texts=[content],
            n_results=num,
            where={"source": role}
        )
    else:
        result = collection.query(
            query_texts=[content],
            n_results=num
        )
    if not result['ids'][0]:
        return "未找到相关记忆。"
    return "\n".join(result['documents'][0])

def online_search(content: str, top=5):
    if not c.online_search:
        print("在线搜索功能未启用")
        return "在线搜索功能未启用"
    import requests
    import time
    print(f"正在搜索：{content}")
    BASE_URL = c.search_base_url
    API_KEY = c.search_api_key
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "messages": [
            {
                "role": "user",
                "content": content,
            }
        ],
        "search_source": "baidu_search_v2",
        "resource_type_filter": [{
                "type": "web",
                "top_k": top
            }]
        }

    for attempt in range(4):
        try:
            resp = requests.post(BASE_URL, json=params, headers=HEADERS, timeout=15)
            http_s = resp.status_code
            if resp.status_code != 200:
                err_body = resp.json() if resp.content else {}
                err_code = err_body.get("error", {}).get("code")
                err_msg = err_body.get("error", {}).get("message", f"HTTP {resp.status_code}")
                if http_s in (500, 502, 503, 429) or err_code in (1, 2):
                    sleep_time = 1.5 * (2 ** attempt)
                    time.sleep(sleep_time)
                    continue
                else:
                    if err_code == 17:
                        print("请求失败，原因：今日免费额度已用完")
                        return "请求失败，原因：今日免费额度已用完"
                    elif http_s in (401, 403):
                        print("请求失败，原因：API Key无效或权限不足")
                        return "请求失败，原因：API Key无效或权限不足"
                    else:
                        print(f"请求失败，HTTP状态码：{resp.status_code}，错误信息：{err_msg}")
                        return f"请求失败，HTTP状态码：{resp.status_code}，错误信息：{err_msg}"

            data: dict= resp.json()
            results = data.get("references", [])
            if not results:
                return "未找到相关内容。"
            result = []
            for item in results:
                item: dict
                result.append({
                    "title" : item.get("title"),
                    "url": item.get("url"),
                    "description": item.get("content")
                })
            
            return_ = []
            for idx, item in enumerate(result, start=1):
                print(f"结果 {idx}:")
                print(f"\t标题: {item['title']}")
                print(f"\t链接: {item['url']}")
                print(f"\t描述: {item['description']}\n")
                return_.append(f"结果 {idx}:[标题: {item['title']},链接: {item['url']},描述: {item['description']}]")
            return "\n".join(return_)
        except requests.exceptions.RequestException as e:
            if attempt < 3:
                time.sleep(1.5 * (2 ** attempt))
                print(f"请求失败，正在重试...（{attempt + 1}/3）")
            else:
                print(f"请求失败，请检查网络连接或稍后再试。{str(e)}")
                return f"请求失败，错误信息：{str(e)}"

def cmd(command: str, content):
    if platform.system() == "Windows":
        ban = ["Format-Volume", "del", "Remove-Item", "Clear-Disk", "Stop-Computer", "Restart-Computer", "shutdown", "Remove-ItemProperty", "Remove-ItemPropertyValue"]
    elif platform.system() == "Linux":
        ban = ["sudo", "rm", "dd", "shutdown", "reboot", "halt", ":(){ :|:& };:", "mkfs", "mkswap", "chmod"]
    else:
        return "不支持的操作系统"

    name = command.split()[0]
    if name.lower() in ban or name[:5] == "/dev/":
        print(f"尝试执行危险命令：{command}，已禁止")
        return "禁止执行危险命令"

    inp = input(f"{c.assistant}尝试执行命令：{command}，说明：{content}。是否同意？（y/n）")
    if inp.lower() != "y":
        print("已拒绝执行命令")
        return "用户拒绝执行命令"

    import subprocess
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True) if platform.system() != "Windows" \
            else subprocess.run(
                ["powershell.exe", "-Command", command],
                capture_output=True,
                text=True
            )
        if result.returncode == 0:
            print(f"命令执行成功，输出：{result.stdout}")
            return f"命令执行成功，输出：{result.stdout}"
        else:
            print(f"命令执行失败，错误信息：{result.stderr}")
            return f"命令执行失败，错误信息：{result.stderr}"
    except Exception as e:
        print(f"命令执行异常，错误信息：{str(e)}")
        return f"命令执行异常，错误信息：{str(e)}"

