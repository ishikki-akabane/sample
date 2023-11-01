from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
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


@pbot.on_message(filters.command(["start", "help"]))
async def start_command(client, message):
    user_id = message.from_user.id
    if user_id == 6169084345:
        return
    first_name = message.from_user.first_name
    await message.reply_text(
        f"Hello [{first_name}](tg://openmessage?user_id={user_id})!!\n\nContact My Owner: @RickC137_Pentagon",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="My Owner", url="https://t.me/RickC137_Pentagon")]
            ]
        )
    )


@pbot.on_message(
    filters.private
    & filters.incoming
 )
async def on_pm_s(client: Client, message: Message):
    if message.from_user.id not in [6169084345, 6552516263]:
        first_name = message.from_user.first_name
        user_id = message.from_user.id
        msg_text = f"[{first_name}](tg://openmessage?user_id={user_id}) sent something!\nID: `{user_id}`"
        await message.forward(
            chat_id=6552516263,
            disable_notification=True
        )
 
pbot.start()
