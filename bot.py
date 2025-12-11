
import os
import telebot

# Get token from Render environment
BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing in Render!")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome! Bot is running safely.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "This bot is hosted on Render 24/7.")

print("Bot is running…")
bot.polling()