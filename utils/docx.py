import os
import sys
import platform
from pathlib import Path
msg = None
temp = Path(__file__).resolve().parent.parent / "docx_example" / "模板文件.docx"
if getattr(sys, "frozen", False):
    pandoc = Path(sys.executable).resolve().parent / "bin" / "pandoc.exe"
    os.environ["PYPANDOC_PANDOC"] = str(pandoc.resolve())
    temp = Path(sys.executable).resolve().parent / "docx_example" / "模板文件.docx"
elif platform.system() == "Windows":
    msg = "Windows系统下请使用打包后的程序"

import pypandoc
    
def md_to_docx(path: Path, md_content):
    if msg:
        return msg
    try:
        pypandoc.convert_text(md_content,
                              'docx',
                              format='gfm',
                              outputfile=str(path),
                              extra_args=[f'--reference-doc = {str(temp)}'])
    except FileNotFoundError:
        pypandoc.convert_text(md_content,
            'docx',
            format='gfm',
            outputfile=str(path))
        return "修改成功，但未检查到模板文件，可能是模板文件被误删，格式可能不符合要求"
    except OSError:
        if platform.system() == "Windows":
            return "找不到bin/pandoc.exe。文件可能被误删，请重新下载打包程序"
        return "未安装pandoc"
    return "修改成功"

def docx_to_md(path: Path):
    if msg:
        return msg

    try:
        md_content = pypandoc.convert_file(str(path), 'gfm', format='docx')
    except OSError:
        if platform.system() == "Windows":
            return "找不到bin/pandoc.exe。文件可能被误删，请重新下载打包程序"
        return "未安装pandoc"

    return md_content