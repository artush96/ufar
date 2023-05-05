import logging
from config import CATEGORY, LOCATION, PRICE_MIN, PRICE_MAX
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from scraper.html_parser_edited import Scraper

logger = logging.getLogger(__name__)


class Messages:

    commands_list = {}

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Hi! I am a bot! Please choose a category from the following list.\n"
            "Real Estate\n"
            "Vehicles\n"
            "Electronics\n"
            "Appliances\n"
            "Home and Garden\n"
            "Clothing and Fashion\n"
            "Baby and Kids\n"
            "Hobbies and Sports\n"
            "Equipment and Materials\n"
            "Pets and Animals\n"
            "Food and Beverages\n"
            "Services\n" 
            "Jobs"
        )
        logger.info('running start')
        self.commands_list = {}

        return CATEGORY

    async def print_msg(self, update, name=None):
        msg = update.message.text
        if name:
            self.commands_list[name] = msg
            print(self.commands_list)

    async def category(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        # global user_cat
        # user_cat = update.message.text
        await update.message.reply_text(
            "Choose the location from the list or send /skip if you want to skip.\n"
            "Yerevan\n"
            "Armavir\n"
            "Ararat\n"
            "Kotayk\n"
            "Shirak\n"
            "Lorri\n"
            "Gegharkunik\n"
            "Syunik\n"
            "Aragatsotn\n"
            "Tavush\n"
            "Vayots Dzor\n"
            "Artsakh\n"
            "International\n"
        )
        logger.info('running category')
        await self.print_msg(update, 'category')

        return LOCATION

    async def location(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # global user_loc
        # user_loc = update.message.text
        await update.message.reply_text(
            "Enter the starting price or send /skip if you want to skip."
        )
        logger.info('running location')
        await self.print_msg(update, 'location')

        return PRICE_MIN

    async def skip_location(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Enter the starting price, or send /skip."
        )
        logger.info('running skip_location')

        return PRICE_MIN

    async def price_min(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # global user_price_min
        # user_price_min = update.message.text
        await update.message.reply_text(
            "Enter the final price."
        )
        logger.info('running price_min')
        await self.print_msg(update, 'price_min')

        return PRICE_MAX

    async def skip_price(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Use /send to send the keywords to the scraper."
        )
        logger.info('running skip_price')

        return ConversationHandler.END

    async def price_max(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # global user_price_max
        # user_price_max = update.message.text
        await update.message.reply_text(
            "Use /send to send the keywords to the scraper."
        )
        logger.info('running price_max')
        await self.print_msg(update, 'price_max')

        return ConversationHandler.END

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "You have cancelled the process."
        )

        return ConversationHandler.END

    async def send_keywords(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        message = Scraper().send_to_scrapper(data=self.commands_list)
        await update.message.reply_text(
            message
        )


    # async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="Available Commands :- \n/status_checker - To get statements from list.am")
    #     logger.info('running help')
    #
    #
    # async def command_listam_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="List.am statements are ready))")
    #     logger.info('running command_listam_status')
