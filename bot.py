import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '8131734989:AAFOB04-0MPifjT5LeVsuvCmWxf13Mf0lEU'
AUTHORIZED_USER_ID = 1088069010

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id

    if user_id != AUTHORIZED_USER_ID:
        await update.message.reply_text("❌ دسترسی غیرمجاز.")
        return

    user_data[user_id] = {}
    await update.message.reply_text("📍 لطفاً مکان را وارد کن:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    text = update.message.text

    if user_id != AUTHORIZED_USER_ID:
        await update.message.reply_text("❌ این ربات فقط مخصوص مدیر هست.")
        return

    if user_id not in user_data:
        await update.message.reply_text("لطفاً اول /start رو بزن.")
        return

    data = user_data[user_id]

    if 'name' not in data:
        data['name'] = text
        await update.message.reply_text("🗺️ حالا آدرس رو وارد کن:")
    elif 'city' not in data:
        data['city'] = text
        await update.message.reply_text("📦 حواله رو وارد کن:")
    elif 'product' not in data:
        data['product'] = text
        await update.message.reply_text("📄 نوع ورق رو وارد کن:")
    elif 'price' not in data:
        data['price'] = text
        await update.message.reply_text("📏 اندازه ورق رو وارد کن:")
    elif 'feature' not in data:
        data['feature'] = text
        await update.message.reply_text("🔢 تعداد برگ رو وارد کن:")
    elif 'contact' not in data:
        data['contact'] = text

        final_text = f"""
سلام وقت بخیر

{data['name']}
-{data['city']}
حواله {data['product']}
ورق {data['price']} {data['feature']} تعداد {data['contact']} برگ
        """.strip()

        await update.message.reply_text("✅ متن نهایی آماده شد:")
        await update.message.reply_text(final_text)

        del user_data[user_id]

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ربات در حال اجراست...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())