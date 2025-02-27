from telegram.ext import CommandHandler, run_async
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list
from telegram import ParseMode, BotCommand

@run_async
def start(update, context):
    LOGGER.info('UID: {} - UN: {} - MSG: {}'.format(update.message.chat.id,update.message.chat.username,update.message.text))
    if update.message.chat.type == "private" :
        sendMessage(f"Hey <b>{update.message.chat.first_name}</b>. Welcome to <b>Search Bot</b>", context.bot, update)
    else :
        sendMessage("Am alive :)", context.bot, update)

@run_async
def log(update, context):
    sendLogFile(context.bot, update)

botcmnd = [
  BotCommand(f'{BotCommands.ListCommand}', ' 🔎 Search on team drive✨')

  ]

def main():

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)

    dispatcher.add_handler(start_handler)

    bot.set_my_commands(botcmnd)

    updater.start_polling()
    LOGGER.info("Yeah am running!")
    updater.idle()

main()
