import re

import matplotlib.pyplot as plt
import requests
from django.conf import settings
from openai import AsyncOpenAI
from telegram import InputFile, Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

telegram_bot_token = "6870648182:AAEXMjbYQe_Uv1qTYZZjHfoYkDj0NKdpVg0"
bot_username = "@DanielFotune_bot"
openai_api_key = "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"
client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
)
print(telegram_bot_token)


def main():
    telegram_bot_token = settings.TELEGRAM_BOT_TOKEN
    bot_username = "@DanielFotune_bot"
    print(telegram_bot_token)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou o bot do Daniel Fortune, como posso te ajudar?",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Qual a sua dúvida?",
    )


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Não entendi o que você deseja, por favor, tente novamente.",
    )


def handle_response(text: str):
    processed_text = text.lower()
    if processed_text == "/start":
        return "Tem uma dúvida? Pergunte-me!"
    elif processed_text == "/help":
        return "Qual a sua dúvida?"
    else:
        return "Não entendi o que você deseja, por favor, tente novamente."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    if message_type == "group":
        if bot_username in text:
            new_text = text.replace(bot_username, "").strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": text}],
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        gpt_text = response.choices[0].message.content

        await update.message.reply_text(gpt_text)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

def latexify(text):
    # Simple conversion to LaTeX - this function can be expanded as needed
    return f'\\text{{ {text} }}'

def plot_formula(formula, filename="formula.png"):
    """Gera uma imagem de uma fórmula LaTeX."""
    print("Generating formula:", formula)
    fig = plt.figure()
    plt.text(
        0.5,
        0.5,
        f"${formula}$",
        fontsize=22,
        ha="center",
        va="center",
    )
    plt.axis("off")
    plt.savefig(filename, format="png", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)
    return filename


def render_message_as_image(text, filename="output.png"):
    # Configura Matplotlib para interpretar LaTeX
    plt.rc("text", usetex=True)
    plt.rc("font", family="sans-serif")

    # Cria uma figura para o texto
    fig = plt.figure(figsize=(10, 5))  # Ajuste o tamanho conforme necessário
    ax = fig.add_subplot(111)

    # Configura o espaço de plotagem
    ax.axis("off")

    # Coloca o texto. Ajuste a posição e o alinhamento conforme necessário
    ax.text(0.5, 0.5, text, fontsize=12, va="center", ha="center", wrap=True)

    # Salva a imagem
    plt.savefig(filename, bbox_inches="tight")
    plt.close()
    return filename



if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(telegram_bot_token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    print("Polling...")
    app.run_polling(poll_interval=3, allowed_updates=Update.ALL_TYPES)
