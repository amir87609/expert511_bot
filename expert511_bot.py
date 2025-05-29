
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# إعداد تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# جلب التوكن من Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

# رسالة الترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Abdullah, these are the deals today. 🇸🇦")

    # تحليل وهمي بسيط - يتم تطويره لاحقًا بمؤشرات حقيقية
    signal = random.choice(["Buy 📈", "Sell 📉"])
    await update.message.reply_text(f"Signal: {signal}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(7467619502:AAGRo3Pe6rrUsSf5rwiIWMbUGhJPekQDllk


).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
