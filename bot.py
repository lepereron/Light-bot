import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# توکن رباتت:
TOKEN = '7646820380:AAFA4hiH2plxRm_-uuQR_NJe-OYTYbEPIEc'
# آیدی تلگرام پیتر:
CHAT_ID = 1088069010

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات روشنه و روی Render اجرا میشه!")

async def notify_me(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="🚀 رباتت به‌درستی روی Render بالا اومد.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # ارسال پیام تست هنگام شروع به پیتر
    app.job_queue.run_once(notify_me, when=3)

    app.run_polling()
