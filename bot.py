import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

addresses = [
    "0xEc082B43D91F4839Bbaad156deAfD322d845F1B2",
    "0x40f44d4eE524eDABCC9147c0103bFb2E8316dA0F",
    "nafiz_003",
    "0x94AEDc599479802313B9B378dc915f12cD59E648",
    "nafiz_005"
]

used_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id in used_users:
        await update.message.reply_text("আপনি ইতিমধ্যে একটি address পেয়ে গেছেন ❗")
        return

    if len(addresses) == 0:
        await update.message.reply_text("দুঃখিত, আর কোনো address নেই ❌")
        return

    address = addresses.pop(0)   # একটার পর একটা দিবে
    used_users.add(user_id)

    await update.message.reply_text(f"আপনার address: {address}")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
