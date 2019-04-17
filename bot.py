from telegram.ext import Updater, CommandHandler
import skylines_api


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


def start(bot, update):
    update.message.reply_text('Welcome to SkylinesBot!')


def last5(bot, update):
    print('last5')
    flights = skylines_api.get_flights_by_airport(42)
    print(flights)
    for flight in flights:
        text = flight["scoreDate"] + '\n' + flight["pilot"]["name"] + '\n' + str(round(flight["distance"]/1000), ) \
               + 'km \n' + flight["model"]["name"] + ' - ' + flight["registration"]
        update.message.reply_text(text)


# read secret bot token from file, remove newline
token_file = open('token.txt', 'r')
secret_token = token_file.read()[:-1]

# init updater
updater = Updater(token=secret_token)
# register command handler for above command functions
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('last5', last5))

# start bot
updater.start_polling()
updater.idle()
