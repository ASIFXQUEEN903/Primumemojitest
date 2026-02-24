from pyrogram import Client, filters
from pyrogram.types import MessageEntity, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import MessageEntityType
from pyrogram.types import InputMediaPhoto, InputMediaVideo

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Custom emoji IDs
CUSTOM_EMOJI_ID_1 = 5210932667452768696  # Balance ke liye
CUSTOM_EMOJI_ID_2 = 5807498479496337570  # Buy Account ke liye

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Welcome message with custom emoji
    welcome_text = "Hello! " + "🌟" + " Welcome to @veloraotpbot\n\n"
    balance_text = "Your Balance: ₹0.00 " + "💰"
    
    full_text = welcome_text + balance_text
    
    # Custom emoji entities for the message
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=7,  # "Hello! " ke baad
            length=1,
            custom_emoji_id=5210932667452768696
        ),
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=len(welcome_text + "Your Balance: ₹0.00 "),
            length=1,
            custom_emoji_id=5807498479496337570
        )
    ]
    
    # Buttons with custom emojis
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="💰 Balance",  # Normal emoji placeholder
                callback_data="balance"
            ),
            InlineKeyboardButton(
                text="🛒 Buy Account",  # Normal emoji placeholder
                callback_data="buy"
            )
        ],
        [
            InlineKeyboardButton(
                text="💸 Sell Accounts",
                callback_data="sell"
            ),
            InlineKeyboardButton(
                text="⚡ Recharge",
                callback_data="recharge"
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 Profile",
                callback_data="profile"
            ),
            InlineKeyboardButton(
                text="📜 History",
                callback_data="history"
            )
        ],
        [
            InlineKeyboardButton(
                text="☰ More",
                callback_data="more"
            ),
            InlineKeyboardButton(
                text="🤝 Refer",
                callback_data="refer"
            )
        ]
    ])
    
    # Send message with buttons
    await message.reply_text(
        full_text,
        entities=entities,
        reply_markup=buttons
    )

# Callback query handler
@app.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    
    responses = {
        "balance": "💰 Your Balance: ₹0.00",
        "buy": "🛒 Buy Account section",
        "sell": "💸 Sell Accounts section", 
        "recharge": "⚡ Recharge section",
        "profile": "👤 Your Profile",
        "history": "📜 Transaction History",
        "more": "☰ More options",
        "refer": "🤝 Refer a Friend"
    }
    
    await callback_query.answer()  # Button press notification
    if data in responses:
        await callback_query.message.reply_text(responses[data])

app.run()
