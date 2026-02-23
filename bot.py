from pyrogram import Client, filters
from pyrogram.types import MessageEntity

API_ID = 1234567
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

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
