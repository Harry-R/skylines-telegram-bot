from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


# read secret bot token from file, remove newline
token_file = open('token.txt', 'r')
secret_token = token_file.read()[:-1]

updater = Updater(secret_token)
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
