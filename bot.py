from pyrogram import Client, filters
import logging


TOKEN = "6169084345:AAHf7ILCo4uSnpp58Z9uuzRSwhC0KRD-RYs"
API_ID = 25629197  # Your API ID
API_HASH = "fd41f8bacda97ab0a3ad120b30339978"  # Your API Hash



FORMAT = "[sample] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[ISHIKKI]')
LOGGER.info("sample is booting up...")

pbot = Client("sample", API_ID, API_HASH, bot_token=TOKEN)

@Client.on_message(filters.command(["start", "help"]) & filters.private)
async def start_command(client, message):
    try:
        user_id = message.from_user.id 
    except:
        return
    first_name = message.from_user.first_name
    exist = registerdb(user_id, first_name)


pbot.start()
