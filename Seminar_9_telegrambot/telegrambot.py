import os
os.system('cls')
# import bot_commands as *
# summ = command.sum_command

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import emoji
import datetime
from daysnewyear import DNY
# import play


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hi! I'm Bot-helper.\nWhat you wanna know?")
    await update.message.reply_text(f'/help - список команд\n/hello - приветствие\n/sum - сумма\n/time - время\n/daysNY - дней до НГ') 

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}! 🤗')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/help - список команд\n/hello - приветствие\n/sum - сумма\n/time - время\n/daysNY - дней до НГ')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def daysny(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{DNY()}')

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text[0] != '/':
        await update.message.reply_text('Просто текст')

        
# async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     mess = update.message.text.split()
#     await update.message.reply_text(int(mess[1]))
#     await update.message.reply_text(play.player(int(mess[1])))

app = ApplicationBuilder().token("6168900290:AAHoak4QChL9ZwkuKtX7nMsU_Qdp29YSrQY").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("daysNY", daysny))
app.add_handler(MessageHandler(None, message))
# app.add_handler(CommandHandler("play", play_command))


print(emoji.emojize(f'This my server :thumbs_up:'))
print("Server start")

app.run_polling()