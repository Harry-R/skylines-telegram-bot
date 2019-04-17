from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


def start(bot, update):
    update.message.reply_text('Welcome to SkylinesBot!')


# read secret bot token from file, remove newline
token_file = open('token.txt', 'r')
secret_token = token_file.read()[:-1]

# init updater
updater = Updater(token=secret_token)
# register command handler for above command functions
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))

# start bot
updater.start_polling()
updater.idle()
