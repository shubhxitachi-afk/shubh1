

import psutil
import os
import time
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_ID
from dixitabot import app, boot, db
from dixitabot.database.chats import add_served_chat
from dixitabot.database.users import add_served_user
from dixitabot.modules.helpers import PNG_BTN
from pyrogram.errors import MessageDeleteForbidden
from dixitabot.modules.helpers.assets import IMG


@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = datetime.now()
    loda = await message.reply_photo(
        photo="https://graph.org/file/210751796ff48991b86a3.jpg",
        caption="pinging...",
    )
    
    # Latency
    ms = (datetime.now() - start).microseconds / 1000
    
    # DB Latency
    db_start = time.time()
    await db.command("ping")
    db_ms = round((time.time() - db_start) * 1000, 2)
    
    # Uptime
    uptime_seconds = int(time.time() - boot)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
    
    # System Info
    process = psutil.Process(os.getpid())
    ram = round(process.memory_info().rss / (1024 * 1024), 2)  # MB
    cpu = process.cpu_percent(interval=0.1)
    try:
        await message.delete()
    except MessageDeleteForbidden:
        pass
    
    await loda.edit_text(
        text=f"""hey baby!!
{app.name} is alive 🥀 and working fine!

<b>bot stats:</b>
- <b>latency:</b> <code>{ms}</code> ms
- <b>db latency:</b> <code>{db_ms}</code> ms
- <b>uptime:</b> <code>{uptime_str}</code>
- <b>ram:</b> <code>{ram}</code> MB
- <b>cpu:</b> <code>{cpu}</code>%""",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
