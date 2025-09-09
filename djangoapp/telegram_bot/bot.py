import logging
import re
import time

from decouple import config
from openai import OpenAI
from rendering_formulas import main as create_image
from save_user_json import operation_in_file
from telegram import (
    KeyboardButton,
    KeyboardButtonPollType,
    Poll,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PollAnswerHandler,
    PollHandler,
    filters,
)
from telegram.helpers import escape_markdown

TELEGRAM_KEY = config("TELEGRAM")
OPENAI = config("OPENAI")
BOT_USERNAME = config("BOT_USERNAME")
FILE_NAME = "user_data.json"

client = OpenAI(api_key=OPENAI)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inform user about what this bot can do"""
    await update.message.reply_text(
        "Ola, me chamo Sofia, faço parte do time de suporte do curso de Econometria Fácil"
        " me envie sua questão sobre econometria que terei o prazer de te ajudar!"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messagem = update.message
    message_type = messagem.chat.type
    text = messagem.text
    message_id = messagem.message_id
    if message_type in ["group", "supergroup"]:
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            gpt_text = new_text
            # thread_id = operation_in_file(client)
            gpt_text = handle_response(new_text)
        else:
            return
    else:
        gpt_text = text
        # thread_id = operation_in_file(client)
        gpt_text = handle_response(text)
    try:
        resp_img, resp_txt = create_image(gpt_text, message_id)
        if resp_img:
            await update.message.reply_photo(
                photo=resp_img,
                caption="Aqui está a resposta para sua solicitação:",
                reply_to_message_id=message_id,
            )
        else:
            await update.message.reply_text(
                text=escape_markdown(resp_txt, version=1),
                reply_to_message_id=message_id,
                parse_mode=ParseMode.MARKDOWN,
            )
    except Exception as e:
        print(e)
        await update.message.reply_text(
            f"Algo deu errado, consulte o suporte humano. informe o id {message_id}",
            reply_to_message_id=message_id,
        )


def handle_response(text):
    thread = client.beta.threads.create()
    thread_id = thread.id
    message = client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=text
    )
    while True:
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id="asst_ScfvIzFIz4wVfKycwIbedfC1",
        )
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            print(messages.data[0].content[0].text.value, "<<<<<<", sep="\n")
            gpt_text = messages.data[0].content[0].text.value
            break
        elif run.status == "failed":
            message = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=text,
            )
            # gpt_text = messages.data[0].content[0].text.value
        else:
            print("Esperando...")
            time.sleep(2)
            # gpt_text = run.status

    gpt_text_clear = limpar_resposta(gpt_text)

    # text_with_formulas = """
    #     A distribuição normal é uma das mais importantes em estatística e econometria, caracterizada por sua forma de sino e simetria em torno da média. Um exemplo clássico de uma distribuição normal é a distribuição das notas de um exame em uma grande população de estudantes. Suponha que as notas de um exame tenham uma média (µ) de 70 e um desvio padrão (σ) de 10. Nesse caso, a distribuição das notas pode ser representada como \(X \sim N(70, 10^2)\).

    #     Isso significa que a maioria dos estudantes terá notas próximas a 70, com menos estudantes obtendo notas muito altas ou muito baixas. A distribuição normal é amplamente utilizada porque muitos fenômenos naturais e sociais tendem a seguir esse padrão, permitindo a aplicação de métodos estatísticos que facilitam a análise e a interpretação dos dados【4:2†source】.

    # """
    # gpt_text_clear = limpar_resposta(text_with_formulas)
    return gpt_text_clear


def limpar_resposta(resposta):
    # Remove os caracteres específicos que causam erro no LaTeX
    resposta_limpa = re.sub(
        r"【.*?†source】", "", resposta
    )  # Remove completamente os blocos que causam erro
    return resposta_limpa


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display a help message"""
    await update.message.reply_text("Use /quiz, /poll or /preview to test this bot.")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


def main():

    app = Application.builder().token(TELEGRAM_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    app.run_polling(poll_interval=3, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
