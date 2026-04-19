import logging
import os
from telegram import Update, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8683570334:AAH7-Zh7UUSamc-Fip2roCFOZ5ZJExitpdo")

logging.basicConfig(level=logging.INFO)

questions = [
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["दिल्ली", "मुंबई", "कोलकाता", "चेन्नई"],
        "answer": 0
    },
    {
        "question": "2 + 2 कितना होता है?",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Quiz Bot!\nType /quiz to start.")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for q in questions:
        await context.bot.send_poll(
            chat_id=update.effective_chat.id,
            question=q["question"],
            options=q["options"],
            type=Poll.QUIZ,
            correct_option_id=q["answer"],
            is_anonymous=False
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))

print("Bot is running...")
app.run_polling()
