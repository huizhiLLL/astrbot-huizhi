import aiohttp

from astrbot.api import star
from astrbot.api.event import AstrMessageEvent, MessageEventResult


class HelpCommand:
    def __init__(self, context: star.Context):
        self.context = context
    async def help(self, event: AstrMessageEvent):
        """查看帮助"""
        msg = f"""会枝の麦麦！
指令合集：（'/'可用'麦麦'代替）
'/群管帮助'：查看群管相关命令
'/meme帮助'：查看表情包合成关键词
'/汤':开启海龟汤游戏
'/画像':分析人物画像
'/cube帮助':查看魔方相关命令
"""

        event.set_result(MessageEventResult().message(msg).use_t2i(False))
