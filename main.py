import telebot
import requests
import re

# YOUR_BOT_TOKEN_HERE နေရာမှာ သင့် Bot Token အမှန်ကို အစားထိုးထည့်ပါ
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    match = re.search(r'(\d+)\s*\((\d+)\)', message.text)
    
    if match:
        user_id = match.group(1)
        zone_id = match.group(2)
        
        # နမူနာ API လင့်ခ်ဖြစ်ပါသည် (အမှန်တကယ် သုံးစွဲရန် API Key ဝယ်ယူထည့်သွင်းရပါမည်)
        api_url = f"https://mobilelegends.com{user_id}&zone={zone_id}"
        
        try:
            response = requests.get(api_url, timeout=10).json()
            if response.get('status') == 'success' or 'name' in response:
                name = response.get('name', 'ရှာမတွေ့ပါ')
                
                reply_text = (
                    f"👤 **Name:** {name}\n"
                    f"🆔 **ID:** {user_id}\n"
                    f"⚔️ **Server:** {zone_id}\n"
                    f"🇲🇲 **Region:** Myanmar"
                )
                bot.reply_to(message, reply_text)
            else:
                bot.reply_to(message, "❌ ဂိမ်း ID သို့မဟုတ် Server မှားယွင်းနေပါသည်။")
        except Exception as e:
            bot.reply_to(message, "⚠️ စနစ်ခေတ္တအဆင်မပြေဖြစ်နေပါသည်။")

bot.polling(none_stop=True)
