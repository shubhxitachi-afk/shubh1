from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from dixitabot import OWNER
from dixitabot import app

DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 owner 🥀", user_id=OWNER, style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="✨ support ✨", url=f"https://t.me/{SUPPORT_GRP}", style=ButtonStyle.PRIMARY),
    ],
    [
        InlineKeyboardButton(
            text="✦ add me baby ✦",
            url=f"https://t.me/{app.username}?startgroup=true",
            style=ButtonStyle.SUCCESS
        ),
    ],
    [
        InlineKeyboardButton(text="<< help >>", callback_data="HELP", style=ButtonStyle.PRIMARY),
    ],
    [
       # InlineKeyboardButton(text="❄️ source ❄️", callback_data="SOURCE", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="☁️ about ☁️", callback_data="ABOUT", style=ButtonStyle.DANGER),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😍 add me baby 😍",
            url=f"https://t.me/{app.username}?startgroup=true",
            style=ButtonStyle.SUCCESS
        ),
    ],
    [
        InlineKeyboardButton(
            text="o close o",
            callback_data="CLOSE",
            style=ButtonStyle.DANGER
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="o back o", callback_data="BACK", style=ButtonStyle.DEFAULT),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 chatbot 🐳", callback_data="CHATBOT_CMD", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="🎄 tools 🎄", callback_data="TOOLS_DATA", style=ButtonStyle.PRIMARY),
    ],
    [
        InlineKeyboardButton(text="o back o", callback_data="BACK", style=ButtonStyle.DEFAULT),
        InlineKeyboardButton(text="o close o", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="o close o", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="enable", callback_data=f"addchat", style=ButtonStyle.SUCCESS),
        InlineKeyboardButton(text="disable", callback_data=f"rmchat", style=ButtonStyle.DANGER),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="soon", callback_data=f"soom", style=ButtonStyle.PRIMARY),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="o back o", callback_data="SBACK", style=ButtonStyle.DEFAULT),
        InlineKeyboardButton(text="o close o", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="o back o", callback_data="CHATBOT_BACK", style=ButtonStyle.DEFAULT),
        InlineKeyboardButton(text="o close o", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="<< help >>", callback_data="HELP", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="🐳 close 🐳", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="<< help >>", url=f"https://t.me/{app.username}?start=help", style=ButtonStyle.PRIMARY
        ),
        InlineKeyboardButton(text="o close o", callback_data="CLOSE", style=ButtonStyle.DANGER),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 support 🎄", url=f"https://t.me/{SUPPORT_GRP}", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="<< help >>", callback_data="HELP", style=ButtonStyle.PRIMARY),
    ],
    [
        InlineKeyboardButton(text="🍾 owner 🍾", user_id=OWNER, style=ButtonStyle.PRIMARY),
     #   InlineKeyboardButton(text="❄️ source ❄️", callback_data="SOURCE", style=ButtonStyle.PRIMARY),
    ],
    [
        InlineKeyboardButton(text="🐳 updates 🐳", url=f"https://t.me/{UPDATE_CHNL}", style=ButtonStyle.PRIMARY),
        InlineKeyboardButton(text="o back o", callback_data="BACK", style=ButtonStyle.DEFAULT),
    ],
]
