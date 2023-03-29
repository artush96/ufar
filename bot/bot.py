import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from config import TOKEN
from commands import command_start, command_listam_status


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class BotBuilder:
    commands = {
        # command_name: function
        'start': command_start,
        'status_checker': command_listam_status
    }

    def __init__(self):
        self.application = ApplicationBuilder().token(TOKEN).build()
        self.register_commands()

    def run_bot(self):
        self.application.run_polling()

    def register_commands(self):
        for name, command in self.commands.items():
            handler = CommandHandler(name, command)
            self.application.add_handler(handler)


if __name__ == '__main__':
    BotBuilder().run_bot()
