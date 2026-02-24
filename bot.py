from pyrogram import Client, filters
from pyrogram.types import MessageEntity, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Custom emoji IDs
CUSTOM_EMOJI_ID_1 = 5210932667452768696  # Balance ke liye
CUSTOM_EMOJI_ID_2 = 5807498479496337570  # Buy ke liye

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Simple text - NO emojis in text
    text = "Hello! Welcome to @veloraotpbot\n\nYour Balance: ₹0.00"
    
    # Entities ko alag se define karo
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=7,  # "Hello! " ke baad (7 characters)
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID_1
        ),
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=len("Hello! Welcome to @veloraotpbot\n\nYour Balance: ₹0.00"),  # Exact length
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID_2
        )
    ]
    
    # Buttons
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
    
    # Message bhejo
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
        "profile": "👤 User Profile",
        "history": "📜 Transaction History",
        "more": "☰ More Options",
        "refer": "🤝 Referral System"
    }
    
    if data in responses:
        await callback_query.message.reply_text(responses[data])

app.run()
