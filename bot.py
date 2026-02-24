from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import MessageEntity
from pyrogram.enums import MessageEntityType

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Tumhari custom emoji IDs
CUSTOM_EMOJI_ID_1 = 5210932667452768696
CUSTOM_EMOJI_ID_2 = 5807498479496337570

app = Client("emoji_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    # Message text
    text = """**HEY!**
User - NOBITA

Welcome To @veloraotpbot
----------------------
Get Telegram Accounts instantly and Securely
• Instant and automatic
• No need to buy from a seller direct
----------------------

**Your Id - 7582601826**
**Your Balance - ₹0.00 ⚡**"""
    
    # Message mein custom emoji
    entities = [
        MessageEntity(
            type=MessageEntityType.CUSTOM_EMOJI,
            offset=len("**HEY!**\nUser - NOBITA\n\nWelcome To @veloraotpbot\n----------------------\nGet Telegram Accounts instantly and Securely\n• Instant and automatic\n• No need to buy from a seller direct\n----------------------\n\n**Your Id - 7582601826**\n**Your Balance - ₹0.00 "),
            length=1,
            custom_emoji_id=CUSTOM_EMOJI_ID_1
        )
    ]
    
    # **BUTTONS में CUSTOM EMOJI - अब possible है!**
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=" Balance",  # Text se pehle emoji aayega
                callback_data="balance",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_1  # 🔥 ये रहा MAGIC!
            ),
            InlineKeyboardButton(
                text=" Buy Account",
                callback_data="buy",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_2
            )
        ],
        [
            InlineKeyboardButton(
                text=" Sell Accounts",
                callback_data="sell",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_1
            ),
            InlineKeyboardButton(
                text=" Recharge",
                callback_data="recharge",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_2
            )
        ],
        [
            InlineKeyboardButton(
                text=" Profile",
                callback_data="profile",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_1
            ),
            InlineKeyboardButton(
                text=" History",
                callback_data="history",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_2
            )
        ],
        [
            InlineKeyboardButton(
                text=" More",
                callback_data="more",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_1
            ),
            InlineKeyboardButton(
                text=" Refer",
                callback_data="refer",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID_2
            )
        ]
    ])
    
    await message.reply_text(
        text=text,
        entities=entities,
        reply_markup=buttons
    )

app.run()
