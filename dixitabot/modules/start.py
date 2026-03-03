

import asyncio
import random

from pyrogram import filters, Client
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from dixitabot import app
from dixitabot.database.chats import add_served_chat
from dixitabot.database.users import add_served_user
from dixitabot.modules.helpers.assets import IMG, STICKER, EMOJIOS
from dixitabot.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@app.on_message(filters.command(["start", "aistart"]))
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"<b>• hey, i am {app.name}</b>\n<b>- an ai based chatbot.</b>\n<b>--------------</b>\n<b>- usage /chatbot [on/off]</b>\n<b>||• hit help button for help||</b>",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@app.on_message(filters.command("help"))
async def help(client: Client, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="<b>hey, pm me for help commands!</b>",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@app.on_message(filters.command("repo"))
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@app.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
