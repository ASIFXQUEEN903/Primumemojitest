from pyrogram import Client, filters
from pyrogram.types import MessageEntity
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

CUSTOM_EMOJI_ID = 5210932667452768696  # INT only

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):

    base_text = "Hi I am custom emoji "
    text = base_text + "⚡"   # Safe visible placeholder

    await message.reply_text(
        text,
        entities=[
            MessageEntity(
                type=MessageEntityType.CUSTOM_EMOJI,
                offset=len(base_text),
                length=1,
                custom_emoji_id=CUSTOM_EMOJI_ID
            )
        ]
    )

app.run()
