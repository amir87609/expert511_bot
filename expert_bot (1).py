
import logging
import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد سجل الأحداث
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# إشارات وهمية مبنية على EMA + RSI + MACD كمثال
def generate_signals():
    signals = [
        "Buy 📈 (EMA Cross + RSI < 30)",
        "Sell 📉 (MACD Divergence + RSI > 70)"
    ]
    return random.sample(signals, 2)

# عند بدء الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Abdullah, these are the deals today. 🇸🇦")
    signals = generate_signals()
    for signal in signals:
        await update.message.reply_text(signal)

# نقطة التشغيل الأساسية
def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN is not set in environment variables.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
