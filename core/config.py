import os
from pathlib import Path
import sys
import random
from dotenv import load_dotenv
from utils import file

def _ensure_value(config, table_path, key, default=None, type_ = bool):
    parts = table_path.split(".")   # 将表路径分割成各个部分

    current = config

    for part in parts:
        if part not in current:
            current[part] = {}  # 若不存在则创建一个空表格
        current = current[part]

    if key not in current:
        current[key] = default  # 若键不存在则设为默认值


    if type_ is not None:
        if type(current[key]) is not type_:
            raise TypeError(f"配置项 {key} 的类型错误，期望 {type_.__name__}，实际 {type(current[key]).__name__}")

    return current[key]

class Config():
    def __init__(self):
        self.tts = None


    @staticmethod
    def exist(path: Path):
        if not path.exists():
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            path.touch()

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

        self.exist(normal_config)
        self.exist(memory_config)
        self.exist(commands_config)
        self.exist(api_config)

        normal_config = file.read(normal_config)
        memory_config = file.read(memory_config)
        commands_config = file.read(commands_config)
        api_config = file.read(api_config)



        _ensure_value(normal_config, "Confirm", "view_files_list", default="看都不让看？", type_=None)
        _ensure_value(normal_config, "Confirm", "delete", default="删掉你也改不了", type_=None)

        # 常规配置
        # Identity
        self.user = _ensure_value(normal_config, "Identity", "user_name", default="User", type_=str)
        self.assistant = _ensure_value(normal_config, "Identity", "assistant_name", default="Assistant", type_=str)
        # Images
        self.upload_images = _ensure_value(normal_config, "Images", "upload", default=False)
        self.files_api = _ensure_value(normal_config, "Images", "Files_API", default=False)
        # Paint
        self.paint = _ensure_value(normal_config, "Paint", "enable", default=False)
        if self.paint:
            if _ensure_value(normal_config, "Paint", "sibling_path", default=True):
                if getattr(sys, "frozen", False):
                    self.comfyui_path = Path(sys.executable).parent.parent / "ComfyUI"
                else:
                    self.comfyui_path = Path(__file__).parent.parent.parent / "ComfyUI"
            else:
                self.comfyui_path = _ensure_value(normal_config, "Paint", "absolute_path", default="", type_=str)
                if not self.comfyui_path:
                    raise ValueError("ComfyUI路径未设置，请检查配置文件中的路径设置。")
                self.comfyui_path = Path(self.comfyui_path)
            if not self.comfyui_path.exists():
                raise ValueError("ComfyUI路径不存在，请检查配置文件中的路径设置。")
            self.comfyui_port = _ensure_value(normal_config, "Paint", "port", default=8188, type_=int)
            self.output_path = _ensure_value(normal_config, "Paint", "custom_output_path", default="", type_=str)
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
        self.paint_confirm = _ensure_value(normal_config, "Confirm", "paint", default=True)
        # 语音合成配置
        self.tts_speed = _ensure_value(normal_config, "Voice", "speed", default=0, type_=int)
        if self.tts_speed < -50 or self.tts_speed > 100:
            raise ValueError("TTS语速必须在[-50, 100]范围内。")
        self.tts_loudness = _ensure_value(normal_config, "Voice", "loudness", default=0, type_=int)
        if self.tts_loudness < -50 or self.tts_loudness > 100:
            raise ValueError("TTS音量必须在[-50, 100]范围内。")
        self.tts_pitch = _ensure_value(normal_config, "Voice", "pitch", default=0, type_=int)
        if self.tts_pitch < -12 or self.tts_pitch > 12:
            raise ValueError("TTS音调必须在[-12, 12]范围内。")
        self.max_parenthesis_length = _ensure_value(normal_config, "Voice", "max_length_to_filter_parenthesis", default=0, type_=int)
        if self.max_parenthesis_length < 0:
            raise ValueError("过滤括号内内容的最大长度必须大于等于0。")

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
        a_k = _ensure_value(api_config, "OpenAI", "api_key", default=["",], type_=list)
        a_k_n = _ensure_value(api_config, "OpenAI.env", "api_key_name", default=["",], type_=list)
        env = _ensure_value(api_config, "OpenAI.env", "env", default=False)
        key = []
        if env:
            load_dotenv()
            for k in a_k_n:
                if k:
                    key.append(os.environ.get(k))
        else:
            for k in a_k:
                if k:
                    key.append(k)
        if key:
            self.api_key = random.choice(key)
        else:
            raise ValueError("没有设置API Key，请在配置文件中设置。")
        self.online_search = _ensure_value(api_config, "OnlineSearch", "enable", default=False)
        s_a_k = _ensure_value(api_config, "OnlineSearch", "api_key", default=["",], type_=list)
        s_a_k_n = _ensure_value(api_config, "OnlineSearch", "api_key_name", default=["",], type_=list)
        self.search_base_url = _ensure_value(api_config, "OnlineSearch", "base_url", default="", type_=str)
        skey = []
        if env:
            for sk in s_a_k_n:
                if sk:
                    skey.append(os.environ.get(sk))
        else:
            for sk in s_a_k:
                if sk:
                    skey.append(sk)
        if self.online_search:
            if skey:
                self.search_api_key = random.choice(skey)
            else:
                raise ValueError("没有设置搜索API Key，请在配置文件中设置。")

        # TTS
        self.tts = _ensure_value(api_config, "TTS", "enable", default=False)
        t_a_k = _ensure_value(api_config, "TTS", "api_key", default=["",], type_=list)
        t_a_k_n = _ensure_value(api_config, "TTS", "api_key_name", default=["",], type_=list)
        tkey = []
        if self.tts:
            if env:
                for tk in t_a_k_n:
                    if tk:
                        tkey.append(os.environ.get(tk))
            else:
                for tk in t_a_k:
                    if tk:
                        tkey.append(tk)
            if tkey:
                self.tts_api_key = random.choice(tkey)
            else:
                raise ValueError("没有设置TTS API Key，请在配置文件中设置。")
            self.tts_model = _ensure_value(api_config, "TTS", "model", default="seed-tts-2.0", type_=str)
            if not self.tts_model:
                raise ValueError("没有设置TTS模型，请在配置文件中设置。")
            self.tts_speaker = _ensure_value(api_config, "TTS", "speaker", default="", type_=str)
            if not self.tts_speaker:
                raise ValueError("没有配置TTS音色，请在配置文件中设置。")

c = Config()
c.load()
