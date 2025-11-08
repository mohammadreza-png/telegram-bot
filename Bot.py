from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات (از BotFather)
TOKEN = "8507658435:AAF6vPExam5dKIrrzT-iNn7TeC0i_v3mxX4"

# رمز ورود مخصوص خودت
PASSWORD = "Mohammadreza@1384"

# لیست کاربران مجاز
authorized_users = set()

# دستور start برای شروع ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in authorized_users:
        await update.message.reply_text("خوش اومدی! دسترسی داری ✅")
    else:
        await update.message.reply_text("برای ورود رمز عبور را بفرست 🔑")

# بررسی پیام‌ها برای رمز و دستورات
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if user_id not in authorized_users:
        if text == PASSWORD:
            authorized_users.add(user_id)
            await update.message.reply_text("رمز درست بود ✅ حالا دسترسی داری!")
        else:
            await update.message.reply_text("رمز اشتباهه ❌")
    else:
        # اگر کاربر مجاز بود و پیام دیگه‌ای فرستاد
        await update.message.reply_text(f"پیام دریافت شد: {text}")

# تابع اصلی اجرای ربات
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات در حال اجراست ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
