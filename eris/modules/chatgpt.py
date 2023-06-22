import requests
from eris import pbot
from pyrogram import Client, filters

@pbot.on_message(filters.command('chat'))
def handle_chat(message):

  command = '/chat'
  text = message.text.replace(command, '', 1).strip()

  if text:
    url = 'https://amirroboti.eliyahost.ir/ApiWeb/ChatGPT1.php?text=' + text
    response = requests.get(url)
    ResponseText = response.text

    bot.edit_message_text(ResponseText)

  else:
    bot.send_message("Report errors at @bloggerminds")
