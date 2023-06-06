from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, RegexHandler, CallbackContext
import requests 
from eris import dispatcher

def handle_message(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    
    if message.text and not message.document:
      response = requests.post(
          "https://api.openai.com/v1/chat/completions",
          headers={
              "Authorization": "Bearer 913d034e16ffc8b9b039feff1968dc6b9fb695acc45b3d8c186c6e3f737d9f4dca9a5b5d115ef697c180883f279424d346d5b94f042fcba1407bd64339da0e4f0c8e90b982e31fa7",
              "Content-Type": "application/json"
          },
          json={
              "model": "text-davinci-003", 
              "messages": [{"role": "system", "content": "You are a bot."}, {"role": "user", "content": message}]
          }
      )
      response_json = response.json()
      bot.send_message(chat_id=update.message.chat_id, text=response_json['choices'][0]['message']['content'])
    
    else:
      bot.send_message("The given message is not supported.")

        
        
CHATGPT_HANDLER = CommandHandler("chatgpt",handle_message,pass_args=True)
dispatcher.add_handler(CHATGPT_HANDLER)
__handlers__ = [CHATGPT_HANDLER]
