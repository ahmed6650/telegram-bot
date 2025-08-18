const express = require("express");
const TelegramBot = require("node-telegram-bot-api");

const TOKEN = "8310692034:AAEV62_5NQos7M8MnxDSWsrt0XugKVbDlV8";  // التوكن حقك
const PORT = process.env.PORT || 3000;

const app = express();

// إنشاء البوت
const bot = new TelegramBot(TOKEN, { polling: true });

// رد بسيط على أي رسالة
bot.on("message", (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, `اهلاً 👋 هذا بوتك شغال! استقبلت رسالتك: "${msg.text}"`);
});

// Render يحتاج سيرفر يشتغل
app.get("/", (req, res) => {
  res.send("البوت شغال ✅");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
