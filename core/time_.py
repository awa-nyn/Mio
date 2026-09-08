from pathlib import Path
import sys
from utils import file
from datetime import datetime
from config import c

def get():
    now = datetime.now()
    ocl = int(now.strftime("%H"))
    period = ""
    if ocl >= 0 and ocl < 6:
        period = "凌晨"
    elif ocl >= 6 and ocl < 11:
        period = "早上"
    elif ocl >= 11 and ocl < 14:
        period = "中午"
    elif ocl >= 14 and ocl < 18:
        period = "下午"
    elif ocl >= 18 and ocl < 20:
        period = "傍晚"
    elif ocl >= 20 and ocl < 24:
        period = "晚上"

    weekdays = ["一", "二", "三", "四", "五", "六", "日"]
    weekday = weekdays[now.weekday()]

    return now.strftime(f"%y-%m-%d 周{weekday} {period}%H:%M")
    
    
def awareness():
    # 获取当前时间对象
    now = datetime.now()

    if getattr(sys, "frozen", False):
        source = Path(sys.executable).parent
    else:
        source = Path(__file__).parent.parent

    # 定位最后一次时间戳路径
    last_path = source / "memory" / "last_timestamp.txt"
    c.exist(last_path)
    last = file.read(last_path)


    # 如果不为空，则计算时间差
    if last:
        last = datetime.strptime(last, "%Y-%m-%d %H:%M")
        delta = now - last
        hour = delta.seconds // 3600

        # 判断日期差
        day = (now.date() - last.date()).days
        new_day = ""
        if day == 1 and now.hour >= 6:
            new_day = "新的一天~\n"

        if delta.days > 0 and delta.days < 7:
            msg = f"[System Message]上次对话：{delta.days}天{hour}小时前\n{new_day}"
        elif delta.days >= 7 and delta.days < 30:
            msg = f"[System Message]上次对话：{delta.days}天前\n"
        elif delta.days >= 30:
            msg = f"[System Message]上次对话：大于一月\n"
        elif delta.days == 0 and hour > 0:
            msg = f"[System Message]上次对话：{hour}小时前\n{new_day}"
        elif delta.days == 0 and hour == 0 and delta.seconds // 60 >= 5:
            msg = f"[System Message]上次对话：{delta.seconds // 60}分钟前\n"
        else:
            msg = "[System Message]上次对话：刚刚\n"
    else:
        msg = "[System Message]首次对话\n"

    file.write(last_path, now.strftime("%Y-%m-%d %H:%M"), mode="w")
    return msg
        