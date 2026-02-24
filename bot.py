from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import MessageEntity
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Custom emoji IDs
CUSTOM_EMOJI_ID = 5210932667452768696

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Text with placeholder
    text = "Welcome to @veloraotpbot  \nYour Balance: ₹0.00"
    # Placeholder at position 24 (space ke jagah)
    
    # Custom emoji entity
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=24,  # space ki position
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID
        )
    ]
    
    # Buttons - normal emojis
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 Balance", callback_data="balance"),
         InlineKeyboardButton("🛒 Buy", callback_data="buy")],
        [InlineKeyboardButton("💸 Sell", callback_data="sell"),
         InlineKeyboardButton("⚡ Recharge", callback_data="recharge")],
        [InlineKeyboardButton("👤 Profile", callback_data="profile"),
         InlineKeyboardButton("📜 History", callback_data="history")],
        [InlineKeyboardButton("☰ More", callback_data="more"),
         InlineKeyboardButton("🤝 Refer", callback_data="refer")]
    ])
    
    await message.reply_text(
        text=text,
        entities=entities,
        reply_markup=buttons
    )

app.run()
