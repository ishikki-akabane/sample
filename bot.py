from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
import asyncio
import logging
import time
import os


TOKEN = "6599175207:AAG4Ow1nXH6LvQeQ-w8Pex6ZKJJ6BQ1WPz0"
API_ID = 25629197  # Your API ID
API_HASH = "fd41f8bacda97ab0a3ad120b30339978"  # Your API Hash


FORMAT = "[ishikki] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[ISHIKKI]')
LOGGER.info("Test server is booting up...")

StartTime = time.time()

app = Client("sample", API_ID, API_HASH, bot_token=TOKEN)


@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id
    current_time = time.time()
    uptime_seconds = current_time - StartTime
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    value = os.getenv('aa')
    print(value)
    final_txt = f"""Hoiiiii!!
    
Uptime: {uptime_hours} hour {uptime_minutes} mins
env : {value}
"""
    await message.reply_text(final_txt)

print("started...")
app.run()
