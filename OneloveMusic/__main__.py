#
# Copyright (C) 2021-2022 by Onelove_Help365 @Github, < https://github.com/TheTeamOnelove >.
# #

# Kanged By © @always_hungry365
# Rocks © @Ourschennai
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Onelove © Onelove


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from OneloveMusic import LOGGER, app, userbot
from OneloveMusic.core.call import Onelove
from OneloveMusic.plugins import ALL_MODULES
from OneloveMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("OneloveMusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("OneloveMusic.plugins" + all_module)
    LOGGER("OneloveMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Onelove.start()
    try:
        await Onelove.stream_call("https://telegra.ph/file/e5938d9ca8fb7c2724f80.jpg")
    except NoActiveGroupCall:
        LOGGER("OneloveMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Onelove.decorators()
    LOGGER("OneloveMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("OneloveMusic").info("Stopping Music Bot")
