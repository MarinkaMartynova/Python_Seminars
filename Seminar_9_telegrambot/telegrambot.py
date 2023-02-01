import os
os.system('cls')
import bot_commands as command

summ = command.sum_command

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')

async def do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Что хочешь узнать?')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)

    
app = ApplicationBuilder().token("TOKEN").build()

print("Server start")
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("do", do))
app.add_handler(CommandHandler("sum", sum))

app.run_polling()