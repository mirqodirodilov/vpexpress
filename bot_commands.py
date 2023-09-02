from aiogram import Bot, Dispatcher, executor, types
from main import *
from funk import *
from main import *


async def set_all_default_commands(bot: Bot):
    await set_default_commands(bot)


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand("/start", "/начать сначала/boshidan boshlash")

        ],
        scope=BotCommandScopeDefault(),
    )
