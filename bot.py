from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, MessageEntity
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Primum emoji IDs
PRIMUM_EMOJI_IDS = {
    "balance": 5210932667452768696,
    "buy": 5807498479496337570,
    "sell": 5210932667452768696,
    "recharge": 5807498479496337570,
    "profile": 5210932667452768696,
    "history": 5807498479496337570,
    "more": 5210932667452768696,
    "refer": 5807498479496337570
}

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Message text mein primum emoji
    text = "⭐️ Welcome! ⚡️"  # Placeholders
    
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=0,  # Pehla character
            length=1,
            custom_emoji_id=PRIMUM_EMOJI_IDS["balance"]
        ),
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=10,  # "Welcome! " ke baad
            length=1,
            custom_emoji_id=PRIMUM_EMOJI_IDS["recharge"]
        )
    ]
    
    # Buttons simple text
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Balance", callback_data="balance"),
         InlineKeyboardButton("Buy", callback_data="buy")],
        [InlineKeyboardButton("Sell", callback_data="sell"),
         InlineKeyboardButton("Recharge", callback_data="recharge")],
        [InlineKeyboardButton("Profile", callback_data="profile"),
         InlineKeyboardButton("History", callback_data="history")],
        [InlineKeyboardButton("More", callback_data="more"),
         InlineKeyboardButton("Refer", callback_data="refer")]
    ])
    
    await message.reply_text(
        text=text,
        entities=entities,
        reply_markup=buttons
    )

app.run()
