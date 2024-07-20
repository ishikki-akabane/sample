from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
import asyncio
import logging


TOKEN = "6386800486:AAHiHVHMDTLoTiFXLnEQwuiS3lGH-s2gTkU"
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

app = Client("sample", API_ID, API_HASH, bot_token=TOKEN)


@app.on_message(filters.command(["start", "help"]))
async def start_command(client, message):
    user_id = message.from_user.id
    
    await message.reply_text("hii")

app.run()
