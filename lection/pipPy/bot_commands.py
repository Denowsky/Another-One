from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log_bot

async def hello_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bot(update, context)
    await update.message.reply_text(f'Oh hi, {update.effective_user.first_name}!')
    
async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bot(update, context)
    await update.message.reply_text(f'Hello, is anybody here?')
    
async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bot(update, context)
    await update.message.reply_text(f'My commands: \n/hello\n/help\n/sum\n/time')
    
async def sum_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bot(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items)>3 or len(items)<3:
        await update.message.reply_text(f'Sorry, mate, it\'s seems wrong...\nGive me: /sum number1 number2\nPlease')
    else: 
        x = int(items[1])
        y = int(items[2])
        await update.message.reply_text(f'{x} + {y} = {x+y}')    

async def time_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bot(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')    

# https://core.telegram.org/api
# https://python-telegram-bot.org/