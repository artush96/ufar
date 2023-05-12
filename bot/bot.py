import logging
from telegram.ext import (ApplicationBuilder,
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    )

from config import TOKEN, CATEGORY, LOCATION, PRICE_MIN, PRICE_MAX
from settings import ROOT_DIR
from commands import Messages

logging.basicConfig(
    filename=f'{ROOT_DIR}/logs/bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class BotBuilder:

    def __init__(self):
        self.application = ApplicationBuilder().token(TOKEN).build()
        self.commands = Messages()
        self.register_commands()

    def run_bot(self):
        self.application.run_polling()


    def register_commands(self):
        # Add conversation handler with the states
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.commands.start)],
            states={
                CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.commands.category)],
                LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.commands.location),
                           CommandHandler("skip", self.commands.skip_location)],
                PRICE_MIN: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.commands.price_min),
                    CommandHandler("skip", self.commands.skip_price),
                ],
                PRICE_MAX: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.commands.price_max)]
            },
            fallbacks=[CommandHandler("cancel", self.commands.cancel)],
        )

        self.application.add_handler(conv_handler)
        self.application.add_handler(CommandHandler("send", self.commands.send_keywords))


if __name__ == '__main__':
    BotBuilder().run_bot()
