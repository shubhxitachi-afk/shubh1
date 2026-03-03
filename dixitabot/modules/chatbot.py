import asyncio
import orjson
import random

from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ChatMemberStatus
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, Message

from dixitabot import LOGGER, app, mongo, redis_db
from dixitabot.modules.helpers.inline import CHATBOT_ON

# Custom adminsOnly decorator
def adminsOnly(permission: str):
    """Decorator to restrict command usage to chat administrators and owners."""
    def decorator(func):
        async def wrapper(client: Client, message: Message):
            try:
                user = await client.get_chat_member(message.chat.id, message.from_user.id)
                if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                    return await func(client, message)
                return
            except UserNotParticipant:
                return
            except Exception as e:
                LOGGER.error(f"Error in adminsOnly decorator: {e}")
        return wrapper
    return decorator

async def smart_match(user_message, database):
    """Smart matching with AI fallback, utilizing Redis caching for exact matches."""
    user_message_lower = user_message.lower().strip()
    
    # 1. Try Redis cache for exact match
    cache_key = f"word_cache_{user_message_lower}"
    if redis_db:
        cached = redis_db.get(cache_key)
        if cached:
            return orjson.loads(cached)
            
    # 1b. Try exact match in DB
    exact = await database.find_one({"word": user_message_lower})
    if exact:
        results = await database.find({"word": user_message_lower}).to_list(length=None)
        clean_results = [{"text": r["text"], "check": r["check"]} for r in results]
        
        if redis_db:
            redis_db.set(cache_key, orjson.dumps(clean_results), ex=86400) # Cache for 24 hours
            
        return clean_results
    
    # 2. Try variations
    variations = [user_message_lower, user_message.strip(), user_message.capitalize()]
    for var in variations:
        result = await database.find_one({"word": var})
        if result:
            return await database.find({"word": var}).to_list(length=None)
    
    # 3. Try partial matching
    words = user_message_lower.split()
    if len(words) > 1:
        for word in words:
            if len(word) > 3:
                result = await database.find_one({"word": word})
                if result:
                    return await database.find({"word": word}).to_list(length=None)
    
    # 4. Try regex (fuzzy)
    for word in words:
        if len(word) > 3:
            regex_result = await database.find({"word": {"$regex": word, "$options": "i"}}).to_list(length=5)
            if regex_result:
                return regex_result
    
    return None

async def process_ai_response(client: Client, message: Message, chatai):
    """Core AI processing logic separated for DRY compliance."""
    if not message.text:
        return
        
    # Non-blocking Chat Action
    asyncio.create_task(client.send_chat_action(message.chat.id, ChatAction.TYPING))
    
    matches = await smart_match(message.text, chatai)
    
    if matches:
        response_data = random.choice(matches)
        response_text = response_data["text"]
        response_type = response_data["check"]
        
        # Auto reaction (30% chance)
        if random.random() < 0.3:
            reactions = ["👍", "❤️", "🔥", "😊", "👏"]
            try:
                await message.react(random.choice(reactions))
            except Exception:
                pass
        
        # Send response gracefully handling FloodWaits
        try:
            if response_type == "sticker":
                await message.reply_sticker(response_text)
            else:
                await message.reply_text(response_text)
        except FloodWait:
            pass



@app.on_message(filters.command("chatbot") & filters.group)
@adminsOnly("can_delete_messages")
async def chaton_(_, m: Message):
    await m.reply_text(
        f"chat: {m.chat.title}\n<b>choose an option to enable/disable chatbot.</b>",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )

@app.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot & ~filters.regex(r"^[!/?@#]"), group=4
)
async def chatbot_smart(client: Client, message: Message):
    chatai = mongo["Word"]["WordDb"]
    DAXX = mongo["DAXXDb"]["DAXX"]
    
    # Check Redis cache for disabled status
    is_DAXX = False
    cache_key = f"chatbot_disabled_{message.chat.id}"
    
    if redis_db:
        cached_status = redis_db.get(cache_key)
        if cached_status is not None:
            is_DAXX = cached_status == "1"
        else:
            is_DAXX_doc = await DAXX.find_one({"chat_id": message.chat.id})
            is_DAXX = bool(is_DAXX_doc)
            redis_db.set(cache_key, "1" if is_DAXX else "0", ex=3600)
    else:
        is_DAXX = await DAXX.find_one({"chat_id": message.chat.id})
    
    if is_DAXX:
        return
    
    # Process AI logic based on contextual triggers
    if not message.reply_to_message:
        await process_ai_response(client, message, chatai)
    elif message.reply_to_message:
        if message.reply_to_message.from_user and message.reply_to_message.from_user.id == client.id:
            await process_ai_response(client, message, chatai)
        else:
            # Self-learning mechanism: learn from user-to-user replies
            if message.reply_to_message.text and not message.reply_to_message.text.startswith(("/", "!", "?", "@", "#")):
                word = message.reply_to_message.text.lower().strip()
                if message.text:
                    # Check if this exact pair already exists to avoid redundant entries
                    exists = await chatai.find_one({"word": word, "text": message.text, "check": "text"})
                    if not exists:
                        await chatai.insert_one({"word": word, "text": message.text, "check": "text"})
                        if redis_db:
                            redis_db.delete(f"word_cache_{word}")
                elif message.sticker:
                    exists = await chatai.find_one({"word": word, "text": message.sticker.file_id, "check": "sticker"})
                    if not exists:
                        await chatai.insert_one({"word": word, "text": message.sticker.file_id, "check": "sticker"})
                        if redis_db:
                            redis_db.delete(f"word_cache_{word}")
