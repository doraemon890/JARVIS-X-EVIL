from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS


@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("» __ᴊᴀʀᴠɪs__")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"__🤖 ᴘɪɴɢ__\n» `{mp} ms`")



@Client.on_message(filters.command('join', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def fuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to join.")
    if hero.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(hero)
        await message.reply_text(f"**Joined ✅**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def leftfuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if hero.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(hero)
        await message.reply_text(f"**Left ❌**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
