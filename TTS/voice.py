import asyncio
import json
from pathlib import Path
import sys
import websockets
from core.config import c
import uuid
import sounddevice as sd
import copy
from TTS.protocols import (
    EventType,
    MsgType,
    finish_connection,
    finish_session,
    receive_message,
    start_connection,
    start_session,
    task_request,
    wait_for_event,
)

URL = "wss://openspeech.bytedance.com/api/v3/tts/bidirection"

class TTS:
    def __init__(self, section_id: str):
        self.section_id = section_id
        self.connect_err = False
        self.api_err = False
        self.recv_task = None

    async def put_text(self, text):
        await self.queue.put(text)

    async def connect(self):
        # 连接服务器
        # 请求头
        header = {
            "X-Api-Key": c.tts_api_key,
            "X-Api-Resource-Id": c.tts_model,
            "X-Api-Connect-Id": str(uuid.uuid4()),  # 暂时不知道有什么用，不过先加上吧
            "X-Control-Require-Usage-Tokens-Return": "*"    # 知道花了多少也改变不了什么
        }
        try:
            self.webs = await websockets.connect(URL, additional_headers=header, max_size=10*1024*1024)  # 看得出来，这个max_size是个立方体(误)
        except Exception as e:
            print("TTS: 连接失败，请检查网络或API Key是否正确", e)
            self.api_err = True
            self.connect_err = True
            return

        try:
            # 开始连接
            await start_connection(self.webs)
            await wait_for_event(self.webs, MsgType.FullServerResponse, EventType.ConnectionStarted)

            self.audio_rcv = False

            # 开始会话
            self.base_rqst = {
                "req_params": {
                    "speaker": c.tts_speaker,
                    "audio_params": {
                        "format": "pcm",
                        "sample_rate": 32000,
                        "speech_rate": c.tts_speed,
                        "loudness_rate": c.tts_loudness,
                    },
                    "addition": {
                        "max_length_to_filter_parenthesis": c.max_parenthesis_length,
                        "disable_markdown_filter": True,
                        "disable_emoji_filter": True,
                        "post_process": {"pitch": c.tts_pitch},
                        "section_id": self.section_id
                    }
                }
            }

            self.session_rqst = copy.deepcopy(self.base_rqst)
            self.session_rqst["event"] = EventType.StartSession
            await start_session(self.webs, json.dumps(self.session_rqst).encode(), self.section_id)
            await wait_for_event(self.webs, MsgType.FullServerResponse, EventType.SessionStarted)
        except Exception:
            await self.webs.close()
            print("TTS: 连接失败，请检查网络是否正常，配置是否正确，或余额是否充足")
            self.connect_err = True


    async def send(self):
        try:
            while True:
                text = await self.queue.get()
                if text == 1:   # 正常结束
                    await finish_session(self.webs, self.section_id)
                    return
                if text == 0:   # 异常结束
                    await finish_session(self.webs, self.section_id)
                    print("TTS: 因对话输出异常中断，TTS发送终止信号")
                    if self.recv_task:
                        self.recv_task.cancel()
                    return
                
                synthesis_rqst = copy.deepcopy(self.base_rqst)
                synthesis_rqst["event"] = EventType.TaskRequest
                synthesis_rqst["req_params"]["text"] = text
                await task_request(self.webs, json.dumps(synthesis_rqst).encode(), self.section_id)
                await asyncio.sleep(0.005)
        except Exception as e:
            print("TTS: 向TTS发送消息失败:", e)
            if self.recv_task:
                self.recv_task.cancel()

    async def receive(self):
        # 创建一个字节数组来存储音频数据
        self.audio_data = bytearray()

        # 循环接收音频数据
        self.stream = None
        try:
            self.stream = sd.OutputStream(   # 播放音频数据
                samplerate=32000,
                channels=1,
                dtype='int32'
            )
            self.stream.start()
            while True:
                msg = await receive_message(self.webs)

                if msg.type == MsgType.FullServerResponse:
                    if msg.event == EventType.SessionFinished:
                        break
                elif msg.type == MsgType.AudioOnlyServer:
                    self.audio_rcv = True
                    self.audio_data.extend(msg.payload)
                    self.stream.write(msg.payload)
                else:
                    print("TTS: 收到未知类型消息:", msg)
                    break
        except asyncio.CancelledError:
            print("TTS: 发送中断，接收任务已取消")
            self.audio_data = None
        except Exception as e:
            print("TTS: 接收音频数据失败:", e)
            self.audio_data = None

    async def save(self):
        if self.audio_data:
            audio_format = self.base_rqst["req_params"]["audio_params"]["format"]
            if getattr(sys, 'frozen', False):
                source = Path(sys.executable).parent
            else:
                source = Path(__file__).parent.parent
            audio_file = source / "audio" / f"{self.section_id}.{audio_format}"
            c.exist(audio_file)
            with open(audio_file, "wb") as f:
                f.write(self.audio_data)

        if self.audio_data is None:
            return
        
        if not self.audio_rcv:
            print("TTS: 没有接收到音频数据")

    async def start(self):
            await self.connect()
            if self.connect_err:
                return
            self.queue = asyncio.Queue()
            # 发送文本
            self.send_task = asyncio.create_task(self.send())
            # 接收音频数据
            self.recv_task = asyncio.create_task(self.receive())

    async def finish(self):
        try:
            await asyncio.gather(self.send_task, self.recv_task, return_exceptions=True)
            await self.save()
        finally:
            # 结束连接
            if self.stream:
                self.stream.stop()
                self.stream.close()
            if not self.connect_err:
                await finish_connection(self.webs)
                await wait_for_event(self.webs, MsgType.FullServerResponse, EventType.ConnectionFinished)
            if not self.api_err:
                await self.webs.close()