from config import OWNER_ID, SUPPORT_GRP
from dixitabot import app

START = f"""
<b>• hey, i am <a href='https://t.me/{app.username}'>{app.name}</a></b>
<b>- an ai based chatbot</b>
<b>--------------</b>
<b>- usage /chatbot [on/off]</b>
<b><spoiler>• hit help button for help.</spoiler></b>
"""

HELP_READ = f"""
<u><b>commands for {app.name}</b></u>
<u><b>are given below!</b></u>
<b>all the commands can be used with:/</b>
<b>--------------</b>
<b><spoiler>©️ <a href='tg://user?id={OWNER_ID}'>Owner</a></spoiler></b>
"""

TOOLS_DATA_READ = f"""
<u><b>tools for {app.name} are:</b></u>
<b>- use /repo for getting source code!</b>
<b>--------------</b>
<b>- use /ping for checking the ping of {app.name}</b>
<b>--------------</b>
<b>- use /id to get your user id, chat id and message id all in a single message.</b>
<b>--------------</b>
<b><spoiler>©️ <a href='tg://user?id={OWNER_ID}'>Owner</a></spoiler></b>
"""

CHATBOT_READ = f"""
<u><b>commands for {app.name}</b></u>
<b>- use /chatbot to enable/disable the chatbot.</b>
<b>• note - the above command for chatbot work in group only!!</b>
<b>---------------</b>
<b><spoiler>©️ <a href='tg://user?id={OWNER_ID}'>Owner</a></spoiler></b>
"""

SOURCE_READ = f"<b>hey, the source code of <a href='https://t.me/{app.username}'>{app.name}</a> is given below.</b>\n<b>please fork the repo &amp; give the star *</b>\n<b>------------------</b>\n<b>here is the <a href='https://github.com/bisug/DAXXCHATBOT'>source code</a></b>\n<b>------------------</b>\n<b>if you face any problem then contact at <a href='https://t.me/{SUPPORT_GRP}'>support chat</a>.</b>\n<b><spoiler>©️ <a href='tg://user?id={OWNER_ID}'>Owner</a></spoiler></b>"

ADMIN_READ = f"soon"

ABOUT_READ = f"""
<b>- <a href='https://t.me/{app.username}'>{app.name}</a> is an ai based chat-bot.</b>
<b>- <a href='https://t.me/{app.username}'>{app.name}</a> replies automatically to a user.</b>
<b>- helps you in activating your groups.</b>
<b>- written in <a href='https://www.python.org'>python</a> with <a href='https://www.mongodb.com'>mongo-db</a> as a database</b>
<b>--------------</b>
<b>- click on the buttons given below for getting basic help and info about <a href='https://t.me/{app.username}'>{app.name}</a></b>
"""
