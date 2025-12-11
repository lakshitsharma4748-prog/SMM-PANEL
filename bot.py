import telebot

# Your correct token with colon
BOT_TOKEN = "8576578203:AAEap2cItQ5YcvbFMIV4qaS9_-cuXEH3064"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome! The bot is running 24/7.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "This is a 24/7 bot hosted on Render.")

print("Bot is running...")
bot.polling()