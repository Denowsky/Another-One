
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("6034780024:AAEdTketU91-EI1x0tA7CS4mJtnTBwsM0yo").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()