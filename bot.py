from pyrogram import Client, filters
from pyrogram.types import MessageEntity
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Tumhari custom emoji ID
CUSTOM_EMOJI_ID = 5210932667452768696

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Text mein placeholder - ek dot (.) jahan emoji aayega
    text = "Hello . Welcome!"
    #             ^ yaha dot hai - iski jagah emoji ayega
    
    # Dot ki position: "Hello " = 6 characters, then dot at position 6
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=6,  # dot ki position
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID
        )
    ]
    
    await message.reply_text(
        text=text,
        entities=entities
    )
    
    # YEHI HAI! Bas itna simple code.
    # Phir dekho custom emoji aayega ya nahi

app.run()
