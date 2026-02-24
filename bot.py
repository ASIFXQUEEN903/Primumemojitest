import os
import requests
import json
from flask import Flask, request
import threading
import time
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8519282511:AAFh9lbDfGlMn2FqjdcIvUsEO_gW8h5yNFw"

# Custom emoji IDs
CUSTOM_EMOJI_ID_1 = 5210932667452768696
CUSTOM_EMOJI_ID_2 = 5807498479496337570

# Bot API URL
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Bot is running!", 200

@app.route(f'/webhook', methods=['POST'])
def webhook():
    """Handle incoming updates"""
    try:
        update = request.get_json()
        logging.info(f"Update received: {update}")
        
        if "message" in update:
            message = update["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")
            
            if text == "/start":
                welcome_text = """<b>HEY!</b>
User - NOBITA

✨ Welcome To @veloraotpbot ✨
----------------------
📱 Get Telegram Accounts instantly and Securely
----------------------

<b>Your Id - 7582601826</b>
<b>Your Balance - ₹0.00</b> 💰"""
                
                # BUTTONS with CUSTOM EMOJI
                keyboard = {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Balance",
                                "callback_data": "balance",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_1)
                            },
                            {
                                "text": "Buy Account",
                                "callback_data": "buy",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_2)
                            }
                        ],
                        [
                            {
                                "text": "Sell Accounts",
                                "callback_data": "sell",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_1)
                            },
                            {
                                "text": "Recharge",
                                "callback_data": "recharge",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_2)
                            }
                        ],
                        [
                            {
                                "text": "Profile",
                                "callback_data": "profile",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_1)
                            },
                            {
                                "text": "History",
                                "callback_data": "history",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_2)
                            }
                        ],
                        [
                            {
                                "text": "More",
                                "callback_data": "more",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_1)
                            },
                            {
                                "text": "Refer",
                                "callback_data": "refer",
                                "icon_custom_emoji_id": str(CUSTOM_EMOJI_ID_2)
                            }
                        ]
                    ]
                }
                
                # Send message
                url = f"{API_URL}/sendMessage"
                payload = {
                    "chat_id": chat_id,
                    "text": welcome_text,
                    "parse_mode": "HTML",
                    "reply_markup": json.dumps(keyboard)
                }
                requests.post(url, json=payload)
                
        elif "callback_query" in update:
            callback = update["callback_query"]
            chat_id = callback["message"]["chat"]["id"]
            data = callback["data"]
            
            # Answer callback query
            answer_url = f"{API_URL}/answerCallbackQuery"
            requests.post(answer_url, json={
                "callback_query_id": callback["id"],
                "text": "Processing..."
            })
            
            # Send response
            responses = {
                "balance": "💰 <b>Your Balance: ₹0.00</b>",
                "buy": "🛒 <b>Buy Account Section</b>\nSelect plan:",
                "sell": "💸 <b>Sell Accounts Section</b>\nUpload screenshot:",
                "recharge": "⚡ <b>Recharge Section</b>\nChoose amount:",
                "profile": "👤 <b>User Profile</b>\nID: 7582601826\nJoined: Today",
                "history": "📜 <b>Transaction History</b>\nNo transactions yet",
                "more": "🔰 <b>More Options</b>\nSettings & Help",
                "refer": "🤝 <b>Referral System</b>\nLink: t.me/veloraotpbot?start=ref"
            }
            
            if data in responses:
                url = f"{API_URL}/sendMessage"
                payload = {
                    "chat_id": chat_id,
                    "text": responses[data],
                    "parse_mode": "HTML"
                }
                requests.post(url, json=payload)
        
        return "OK", 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Error", 500

def set_webhook():
    """Set webhook for bot"""
    time.sleep(5)
    app_name = os.environ.get('HEROKU_APP_NAME', 'your-app-name')
    webhook_url = f"https://{app_name}.herokuapp.com/webhook"
    
    url = f"{API_URL}/setWebhook"
    try:
        response = requests.post(url, json={"url": webhook_url})
        logging.info(f"Webhook set: {response.json()}")
    except Exception as e:
        logging.error(f"Webhook error: {e}")

if __name__ == "__main__":
    # Set webhook
    threading.Thread(target=set_webhook).start()
    
    # Run app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
