from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6034780024:AAEdTketU91-EI1x0tA7CS4mJtnTBwsM0yo").build()

app.add_handler(CommandHandler("hello", hello_bot))
app.add_handler(CommandHandler("start", start_bot))
app.add_handler(CommandHandler("help", help_bot))
app.add_handler(CommandHandler("sum", sum_bot))
app.add_handler(CommandHandler("time", time_bot))

print("server started")

app.run_polling()