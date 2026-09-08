from pathlib import Path
import sys
from utils import file
import random

def _ensure_value(config, table_path, key, default=None, type_ = bool):
    parts = table_path.split(".")   # 将表路径分割成各个部分

    current = config

    for part in parts:
        if part not in current:
            current[part] = {}  # 若不存在则创建一个空表格
        current = current[part]

    if key not in current:
        current[key] = default  # 若键不存在则设为默认值

    if not type_:
        if type(current[key]) != type_:
            raise TypeError(f"配置项 {key} 的类型错误，期望 {type_}，实际 {type(current[key]).__name__}")

    return current[key]

class Config():
    def __init__(self):
        self.user = None
        self.assistant = None
        self.upload_images = None
        self.files_api = None
        self.image_memory = None
        self.read = None
        self.write_a = None
        self.write_w = None
        self.create = None
        self.move = None
        self.copy = None
        self.rename = None
        self.info = None
        self.search = None
        self.lsr = None
        self.overwrite_docx = None
        self.h_days = None
        self.h_tokens = None
        self.q = None
        self.rc = None
        self.i = None
        self.di = None
        self.rv = None
        self.lm = None
        self.dm = None
        self.reset = None
        self.base_url = None
        self.model = None
        self.tool = None
        self.reasoning_effort = None
        self.extra_body = None
        self.think_output = None
        self.api_key = None

    def exist(path: Path):
        if not path.exists():
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            path.touch()
        return file.read(path)

    def load(self):
        # 获取配置文件路径
        if getattr(sys, "frozen", False):
            source = Path(sys.executable).parent
        else:
            source = Path(__file__).parent.parent
        normal_config = source / "config" / "常规配置.toml"
        memory_config = source / "config" / "记忆配置.toml"
        commands_config = source / "config" / "指令配置.toml"
        api_config = source / "config" / "API配置.toml"

        normal_config = self.exist(normal_config)
        memory_config = self.exist(memory_config)
        commands_config = self.exist(commands_config)
        api_config = self.exist(api_config)

        _ensure_value(normal_config, "Confirm", "view_files_list", default="看都不让看？", type_=None)
        _ensure_value(normal_config, "Confirm", "delete", default="删掉你也改不了", type_=None)

        # 常规配置
        # Identity
        self.user = _ensure_value(normal_config, "Identity", "user_name", default="User", type_=str)
        self.assistant = _ensure_value(normal_config, "Identity", "assistant_name", default="Assistant", type_=str)
        # Images
        self.upload_images = _ensure_value(normal_config, "Images", "upload", default=False)
        self.files_api = _ensure_value(normal_config, "Images", "Files_API", default=False)
        # Confirm
        self.read = _ensure_value(normal_config, "Confirm", "view_file", default=False)
        self.write_a = _ensure_value(normal_config, "Confirm", "append_file", default=True)
        self.write_w = _ensure_value(normal_config, "Confirm", "overwrite_file", default=True)
        self.create = _ensure_value(normal_config, "Confirm", "create_file", default=False)
        self.move = _ensure_value(normal_config, "Confirm", "move_file", default=True)
        self.copy = _ensure_value(normal_config, "Confirm", "copy_file", default=True)
        self.rename = _ensure_value(normal_config, "Confirm", "rename_file", default=False)
        self.info = _ensure_value(normal_config, "Confirm", "get_file_info", default=False)
        self.search = _ensure_value(normal_config, "Confirm", "search_file", default=False)
        self.lsr = _ensure_value(normal_config,"Confirm" ,"view_files_list_recursive", default=True)
        self.overwrite_docx = _ensure_value(normal_config, "Confirm", "overwrite_docx", default=True)

        # 记忆配置
        self.h_days = _ensure_value(memory_config, "Memory", "max_history_days", default=7, type_=int)
        self.h_tokens = _ensure_value(memory_config, "Memory", "max_history_tokens", default=64000, type_=int)

        # 指令配置
        self.q = "/" + _ensure_value(commands_config, "Commands", "quit", default="q", type_=str)
        self.rc = "/" + _ensure_value(commands_config, "Commands", "reload_config", default="rc", type_=str)
        self.i = "/" + _ensure_value(commands_config, "Commands", "upload_images", default="i", type_=str)
        self.di = "/" + _ensure_value(commands_config, "Commands", "delete_images", default="di", type_=str)
        self.rv = "/" + _ensure_value(commands_config, "Commands", "revoke", default="rv", type_=str)
        self.lm = "/" + _ensure_value(commands_config, "Commands", "list_memory", default="lm", type_=str)
        self.dm = "/" + _ensure_value(commands_config, "Commands", "delete_memory", default="dm", type_=str)
        self.reset = "/" + _ensure_value(commands_config, "Commands", "reset_agent", default="reset", type_=str)

        # API配置
        # OpenAI
        self.base_url = _ensure_value(api_config, "OpenAI", "base_url", default="", type_=str)
        self.model = _ensure_value(api_config, "OpenAI", "model", default="", type_=str)
        self.tool = _ensure_value(api_config, "OpenAI", "tool", default=True)
        self.reasoning_effort = _ensure_value(api_config, "OpenAI", "reasoning_effort", default="medium", type_=str)
        self.extra_body = _ensure_value(api_config, "OpenAI", "extra_body", default={}, type_=dict)
        self.think_output = _ensure_value(api_config, "OpenAI", "think_output", default=True)
        # api_key
        _ensure_value(api_config, "OpenAI", "api_key", default=["",], type_=list)
        _ensure_value(api_config, "OpenAI.env", "api_key_name", default=["",], type_=list)
        self.env = _ensure_value(api_config, "OpenAI.env", "env", default=False)
        a_k = api_config["OpenAI"]["api_key"]
        a_k_n = api_config["OpenAI.env"]["api_key_name"]
        key = []
        if self.env:
            for k in a_k_n:
                if not k:
                    key.append(k)
        else:
            for k in a_k:
                if not k:
                    key.append(k)
        self.api_key = random.choice(key)


c = Config()
c.load()
