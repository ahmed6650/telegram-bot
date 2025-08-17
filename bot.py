import os
import telebot

# اقرأ التوكن من متغير البيئة BOT_TOKEN
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is missing")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
# Telegram Bot (Render)

## الملفات
- bot.py
- requirements.txt
- Procfile

## الخطوات المختصرة
1) ارفع هذه الملفات إلى مستودع GitHub جديد.
2) افتح Render > New > Background Worker > اختر المستودع.
3) Start Command:  `python bot.py`
4) Environment > Add Variable:
   - Key: `BOT_TOKEN`
   - Value: (ضع التوكن من BotFather)
5) Deploy — وسيعمل البوت 24/7.

*ملاحظة:* إذا أنشأت Web Service بالخطأ سيفشل لأنه لا يستمع على منفذ. اختر Background Worker.

@bot.message_handler(commands=["start"])pyTelegramBotAPI==4.12.0

def start(message):worker: python bot.py

    bot.reply_to(message, "👋 أهلاً! البوت شغال على Render ✅")

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.reply_to(message, "الأوامر المتاحة:\n/start - بدء\n/help - مساعدة")

# Echo لأي رسالة (تجريبي)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    # polling بلا نهاية
    bot.infinity_polling()
