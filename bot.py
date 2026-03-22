import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

PRIVATE_CHANNEL_ID = -1003861152442 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            msg_id = int(context.args[0])
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,
                from_chat_id=PRIVATE_CHANNEL_ID,
                message_id=msg_id
            )
        except Exception:
            pass
    else:
        await update.message.reply_text("স্বাগতম! ভিডিও দেখতে আমাদের ওয়েবসাইট ভিজিট করুন।")

if __name__ == '__main__':
    token = '8775617363:AAHRI-Mjze7F41vxs32Bj_2lXU5ym_b37Ro'
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()
