import logging
import sys
import time

# Importe o módulo principal do seu bot aqui
from main import main
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.INFO)


class BotFileHandler(FileSystemEventHandler):
    def __init__(self, bot_main):
        super().__init__()
        self.bot_main = bot_main

    def on_any_event(self, event):
        if event.is_directory:
            return
        logging.info(f"Detected file change: {event.src_path}")
        self.bot_main.restart()


class BotWatcher:
    def __init__(self, bot_main):
        self.bot_main = bot_main
        self.observer = Observer()
        self.event_handler = BotFileHandler(self.bot_main)

    def start(self):
        self.observer.schedule(self.event_handler, ".", recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()


class BotMain:
    def __init__(self):
        # Inicialize o seu bot aqui
        self.bot = main()  # Substitua "main" pelo método de inicialização do seu bot

    def restart(self):
        logging.info("Restarting bot...")
        self.bot.stop_polling()
        self.bot.start_polling()


if __name__ == "__main__":
    bot_main = BotMain()
    bot_watcher = BotWatcher(bot_main)
    bot_watcher.start()
