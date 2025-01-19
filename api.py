import os
import openai
from aiogram import BOT,Dispatcher, execute , types

bot = BOT(token = 'BOT Token')
dp = Dispatcher(bot)

open.ai_key = "CHAT GPT API KEY"

@dp.message_handle(commands = ['start' , 'help'])
async def welcome(message: type.Message):
    await message.replay('Hello! Iam aisendchatbot.Ask me something')

@dp.message_handle()
async def welcome(message: type.Message):
    response = openai.Completion.create(  
    model = "text-davinci-003" , 
    prompt=message.text,
    tempurature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)
await message.replay(response.choices[0].text)

if __name__ == "__main__":
  execute.start_polling(dp)
