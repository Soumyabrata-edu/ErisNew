import requests
from eris import pbot
from pyrogram import Client, filters
from telegram import Update, Bot

@pbot.on_message(filters.command('ask'))
def handle_chat(update: Update, bot: Bot):

  utext = update.message.text
  text = utext.text.replace('/ask', '', 1).strip() 
  
  if text:
    
    url = 'https://amirroboti.eliyahost.ir/ApiWeb/ChatGPT1.php?text=' + text
    response = requests.get(url)
    ResponseText = response.text

    bot.send_message(chat_id=update.message.chat_id, text= ResponseText)

  else:
    bot.send_message("Report errors at @bloggerminds")
