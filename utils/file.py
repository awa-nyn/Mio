import yaml
from ruamel.yaml import YAML
import tomlkit
import json
import os
from configparser import ConfigParser
from dotenv import load_dotenv
    
# 打开文件操作

# 只读模式打开文件，读取文件内容并返回
def read(file_path, encoding='utf-8'):
    # 使用with语句可以确保文件在使用后正确关闭，避免资源泄漏。
    file_path = str(file_path)
    with open(file_path, 'r', encoding=encoding) as f:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(f)  # 使用yaml库读取YAML文件内容并返回
        elif file_path.endswith('.toml'):
            return tomlkit.load(f)  # 使用tomlkit库读取TOML文件内容并返回
        elif file_path.endswith('.json'):
            return json.load(f)  # 使用json库读取JSON文件内容并返回
        elif file_path.endswith('.ini'):
            config = ConfigParser()
            config.read_file(f)  # 使用ConfigParser读取INI文件内容
            return {section: dict(config.items(section)) for section in config.sections()}  # 将INI内容转换为字典并返回
        elif file_path.endswith('.env'):
            load_dotenv(f)  # 使用dotenv库加载.env文件内容
            return dict(os.environ)  # 返回当前环境变量的字典表示
        else:
            return f.read()  # 如果文件类型不匹配，直接读取文件内容并返回

def write(file_path, content, mode='a', encoding='utf-8'):
    file_path = str(file_path)
    with open(file_path, mode, encoding=encoding) as f:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            yaml = YAML()
            yaml.preserve_quotes = True  # 保留引号
            yaml.dump(content, f)  # 使用ruamel.yaml库写入YAML文件
        elif file_path.endswith('.toml'):
            tomlkit.dump(content, f)  # 使用tomlkit库写入TOML文件
        elif file_path.endswith('.json'):
            json.dump(content, f, ensure_ascii=False, indent=4)  # 使用json库写入JSON文件
        elif file_path.endswith('.jsonl'):
            text = json.dumps(content, ensure_ascii=False) + '\n'
            f.write(text)
        elif file_path.endswith('.ini'):
            config = ConfigParser()
            for section, values in content.items():
                config[section] = values  # 将字典内容转换为INI格式
            config.write(f)  # 使用ConfigParser写入INI文件
        else:
            f.write(content)  # 如果文件类型不匹配，直接写入内容