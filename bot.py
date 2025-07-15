import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '7646820380:AAFA4hiH2plxRm_-uuQR_NJe-OYTYbEPIEc'
CHAT_ID = 1088069010

async def start_command(update, context):
    await update.message.reply_text("✅ ربات روشن است!")

async def send_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="📡 بات با موفقیت اجرا شد", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.job_queue.run_once(send_message, when=3)

    app.run_polling()
