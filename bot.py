import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

addresses = [
    "0xEc082B43D91F4839Bbaad156deAfD322d845F1B2",
    "0x40f44d4eE524eDABCC9147c0103bFb2E8316dA0F",
    "nafiz_003",
    "0x94AEDc599479802313B9B378dc915f12cD59E648",
    "nafiz_005"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = random.choice(addresses)
    await update.message.reply_text(address)

app = ApplicationBuilder().token("8098593416:AAGeexlY8B_RvMYB0DR4Tv2cv8YmBNo25U8").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
