from pyrogram import Client, filters
from pyrogram.types import MessageEntity, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Tumhari dono custom emoji IDs
CUSTOM_EMOJI_ID_1 = 5210932667452768696
CUSTOM_EMOJI_ID_2 = 5807498479496337570

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Message text with placeholders
    text = """**HEY!**
User - NOBITA

Welcome To @veloraotpbot
----------------------
Get Telegram Accounts instantly and Securely
• Instant and automatic
• No need to buy from a seller direct
----------------------

**Your Id - 7582601826**
**Your Balance - ₹0.00 ⚡**"""  # ⚡ placeholder for custom emoji
    
    # Custom emoji entity
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=len("**HEY!**\nUser - NOBITA\n\nWelcome To @veloraotpbot\n----------------------\nGet Telegram Accounts instantly and Securely\n• Instant and automatic\n• No need to buy from a seller direct\n----------------------\n\n**Your Id - 7582601826**\n**Your Balance - ₹0.00 "),
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID_1
        )
    ]
    
    # Buttons with normal emojis
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💰 Balance", callback_data="balance"),
            InlineKeyboardButton("🛒 Buy Account", callback_data="buy")
        ],
        [
            InlineKeyboardButton("💸 Sell Accounts", callback_data="sell"),
            InlineKeyboardButton("⚡ Recharge", callback_data="recharge")
        ],
        [
            InlineKeyboardButton("👤 Profile", callback_data="profile"),
            InlineKeyboardButton("📜 History", callback_data="history")
        ],
        [
            InlineKeyboardButton("☰ More", callback_data="more"),
            InlineKeyboardButton("🤝 Refer", callback_data="refer")
        ]
    ])
    
    await message.reply_text(
        text=text,
        entities=entities,
        reply_markup=buttons
    )

@app.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    await callback_query.answer()
    
    responses = {
        "balance": "💰 Your Balance: ₹0.00",
        "buy": "🛒 Buy Account - Coming Soon",
        "sell": "💸 Sell Accounts - Coming Soon",
        "recharge": "⚡ Recharge - Coming Soon",
        "profile": "👤 Your Profile",
        "history": "📜 Transaction History",
        "more": "☰ More Options",
        "refer": "🤝 Referral System"
    }
    
    if data in responses:
        await callback_query.message.reply_text(responses[data])

app.run()
