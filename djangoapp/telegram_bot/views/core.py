import io

import matplotlib.pyplot as plt
import openai
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, MessageHandler,
                          Updater, filters)

# Your OpenAI and Telegram Bot API keys
OPENAI_API_KEY = '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'
TELEGRAM_TOKEN = '6870648182:AAEXMjbYQe_Uv1qTYZZjHfoYkDj0NKdpVg0'

openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Send me a complex formula and I will render it.')

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    formula = response['choices'][0]['message']['content']
    img = create_formula_image(formula)
    update.message.reply_photo(photo=img)

def create_formula_image(formula):
    buffer = io.BytesIO()
    plt.figure(figsize=(6, 1))
    plt.text(0.5, 0.5, f'${formula}$', fontsize=16, ha='center', va='center')
    plt.axis('off')
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    plt.close()
    return buffer

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
