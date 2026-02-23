from pyrogram import Client, filters
from pyrogram.types import MessageEntity

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8373170298:AAEVgziTeeHsKBCCK2X-_7pCcJ_kaeroz5A"

CUSTOM_EMOJI_ID = "6289579292565178263"

app = Client(
    "emoji_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):

    text = "Hi I am custom emoji A"
    
    await message.reply_text(
        text,
        entities=[
            MessageEntity(
                type="custom_emoji",
                offset=len("Hi I am custom emoji "),  # emoji position
                length=1,
                custom_emoji_id=CUSTOM_EMOJI_ID
            )
        ]
    )

print("Bot Started...")
app.run()
