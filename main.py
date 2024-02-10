import asyncio
import importlib
from JARVIS import ALL_MODULES
from pyrogram import idle
from config import client, client2, client3, client4, client5, client6, client7, client8, client9, client10
from config import *


async def main():
    if client:
        try:
            await client.start()
            await client.join_chat("BWANDARLOK")
            await client.join_chat("TEAM_CDX")
            await client.join_chat("GLACEON_CHATS")
            await client.join_chat("THE_GLACEON")
            await client.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client2:
        try:
            await client2.start()
            await client2.join_chat("BWANDARLOK")
            await client2.join_chat("TEAM_CDX")
            await client2.join_chat("GLACEON_CHATS")
            await client2.join_chat("THE_GLACEON")
            await client2.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client3:
        try:
            await client3.start()
            await client3.join_chat("BWANDARLOK")
            await client3.join_chat("TEAM_CDX")
            await client3.join_chat("GLACEON_CHATS")
            await client3.join_chat("THE_GLACEON")
            await client3.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client4:
        try:
            await client4.start()
            await client4.join_chat("BWANDARLOK")
            await client4.join_chat("TEAM_CDX")
            await client4.join_chat("GLACEON_CHATS")
            await client4.join_chat("THE_GLACEON")
            await client4.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client5:
        try:
            await client5.start()
            await client5.join_chat("BWANDARLOK")
            await client5.join_chat("TEAM_CDX")
            await client5.join_chat("GLACEON_CHATS")
            await client5.join_chat("THE_GLACEON")
            await client5.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client6:
        try:
            await client6.start()
            await client6.join_chat("BWANDARLOK")
            await client6.join_chat("TEAM_CDX")
            await client6.join_chat("GLACEON_CHATS")
            await client6.join_chat("THE_GLACEON")
            await client6.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client7:
        try:
            await client7.start()
            await client7.join_chat("BWANDARLOK")
            await client7.join_chat("TEAM_CDX")
            await client7.join_chat("GLACEON_CHATS")
            await client7.join_chat("THE_GLACEON")
            await client7.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client8:
        try:
            await client8.start()
            await client8.join_chat("BWANDARLOK")
            await client8.join_chat("TEAM_CDX")
            await client8.join_chat("GLACEON_CHATS")
            await client8.join_chat("THE_GLACEON")
            await client8.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client9:
        try:
            await client9.start()
            await client9.join_chat("BWANDARLOK")
            await client9.join_chat("TEAM_CDX")
            await client9.join_chat("GLACEON_CHATS")
            await client9.join_chat("THE_GLACEON")
            await client9.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))

    if client10:
        try:
            await client10.start()
            await client10.join_chat("BWANDARLOK")
            await client10.join_chat("TEAM_CDX")
            await client10.join_chat("GLACEON_CHATS")
            await client10.join_chat("THE_GLACEON")
            await client10.join_chat("CDX_WORLD")
        except Exception as e:
            print(str(e))
    for all_module in ALL_MODULES:
        importlib.import_module("JARVIS" + all_module)
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
