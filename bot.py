import os
import telebot

# الحصول على التوكن من المتغيرات
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is missing")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# أمر بدء التشغيل
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "أهلاً! البوت شغال ✅")

# أمر بسيط للرد على /help
@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "اكتب /start لتجربة البوت.")

# تشغيل البوت
bot.infinity_polling()
