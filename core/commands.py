from pathlib import Path
import sys
import sqlite3
from core.config import c

def act(command):
    commands = {
        "quit": c.q,
        "reload_config": c.rc,
        "upload_images": c.i,
        "delete_image": c.di,
        "revoke": c.rv,
        "list_memory": c.lm,
        "delete_memory": c.dm,
        "reset_agent": c.reset,}

    repeat = set()

    for cmd in commands.values():
        repeat.add(cmd)

    if len(repeat) != len(commands):
        raise ValueError("指令配置中存在重复的指令，请检查配置文件。")
    # 退出
    if command == commands["quit"]:
        print("对话结束...")
        sys.exit(0)
    # 重新加载配置文件
    elif command == commands["reload_config"]:
        c.load()
        print("配置文件已重新加载。")
        return False    # 不退出循环
    # 上传图片
    elif command == commands["upload_images"]:
        if not c.upload_images:
            return None
        from core.images import upload_images
        images = upload_images()
        if images:
            return images
        elif images is None:
            return False
    # 删除图片    
    elif command[:len(commands["delete_image"])+1] == commands["delete_image"]+" " or command == commands["delete_image"]:
        if len(command) == len(commands["delete_image"]):
            return {"di": 0}
        elif len(command) > len(commands["delete_image"]):
            idx = command[len(commands["delete_image"])+1:]
            if not idx.isdigit() or int(idx) < 0:
                print("请输入一个非负整数。")
                return False
            idx = int(idx)
            return {"di": idx}
    # 撤销操作    
    elif command[:len(commands["revoke"])+1] == commands["revoke"]+" " or command == commands["revoke"]:
        if len(command) == len(commands["revoke"]):
            return {"rv": 1}
        elif len(command) > len(commands["revoke"]):
            idx = command[len(commands["revoke"])+1:]
            if not idx.isdigit() or int(idx) < 1:
                print("请输入一个正整数。")
                return False
            idx = int(idx)
            return {"rv": idx}
    # 列出记忆    
    elif command == commands["list_memory"]:
        if getattr(sys, "frozen", False):
            source = Path(sys.executable).parent
        else:
            source = Path(__file__).parent.parent
        db_path = source / "memory" / "memory.db"
        if not db_path.exists():
            print("尚未指定任何记忆。")
            return False
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='specified_memory'")
            if not cursor.fetchone():
                print("尚未指定任何记忆。")
                return False
            cursor.execute("SELECT * FROM specified_memory")
            memories = cursor.fetchall()
            if not memories:
                print("尚未指定任何记忆。")
                return False
            print("当前记忆列表：")
            print("序号\t记忆内容")
            for memory in memories:
                print(f"{memory[0]}\t{memory[1]}")
            return False
    # 删除记忆    
    elif  (len(command) == len(commands["delete_memory"]) and command == commands["delete_memory"]):
        print("请输入要删除的记忆序号，例如：/dm 1")
        return False
    elif command[:len(commands["delete_memory"])+1] == commands["delete_memory"]+" ":
        idx = command[len(commands["delete_memory"])+1:]
        if not idx.isdigit():
            print("请在空格后输入要删除的记忆序号")
            return False
        idx = int(idx)
        if getattr(sys, "frozen", False):
            source = Path(sys.executable).parent
        else:
            source = Path(__file__).parent.parent
        db_path = source / "memory" / "memory.db"
        if not db_path.exists():
            print("尚未指定任何记忆。")
            return False
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='specified_memory'")
            if not cursor.fetchone():
                print("没有任何记忆可以删除。")
                return False
            cursor.execute("DELETE FROM specified_memory WHERE id = ?", (idx,))
            if cursor.rowcount == 0:
                print(f"未找到序号为 {idx} 的记忆。")
            else:
                print(f"已删除序号为 {idx} 的记忆。")
            return False
    # 重置智能体
    elif command == commands["reset_agent"]:
        msg = input("确定要重置智能体吗？这将清除所有记忆！(y/n): ")
        while True:
            if msg.lower() == "y":
                if getattr(sys, "frozen", False):
                    source = Path(sys.executable).parent
                else:
                    source = Path(__file__).parent.parent
                memory_path = source / "memory"
                if memory_path.exists():
                    from tools import manager
                    tool = manager.ToolManager(memory_path)
                    tool._del()
                    print("智能体已重置，所有记忆已清除。")
                    sys.exit(0)
                else:
                    print("智能体未初始化，无需重置。")
                    return False
            elif msg.lower() == "n":
                print("已取消重置操作。")
                return False