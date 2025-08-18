import telebot
import os
from flask import Flask, request

#8310692034:AAEV62_5NQos7M8MnxDSWsrt0XugKVbDlV8
TOKEN = "8310692034:AAEV62_5NQos7M8MnxDSWsrt0XugKVbDlV8"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً! البوت شغال ✅\nاكتب /ping للتجربة.")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "pong 🏓")

# مسار استقبال رسائل تيليجرام
@app.route("/" + TOKEN, methods=['POST'])
def receive_update():
    update = telebot.types.Update.de_json(request.get_data().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# إعداد/تجديد الويبهوك عند فتح الصفحة الرئيسية
@app.route("/", methods=['GET'])
def set_webhook():
    base_url = request.host_url  # مثل https://your-app.onrender.com/
    webhook_url = base_url + TOKEN
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    return f"Webhook set to: {webhook_url}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
