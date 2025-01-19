# https://t.me/aisendchatbot
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
import etherscan
import requests
import random, json
import base64
from PIL import Image

# pip install python-telegram-bot
# pip install openai

TOKEN: Final = r'Enter Telegram Bot Token'
BOT_USERNAME: Final = '@aisendchatbot'
ETHSCAN = r'ETH API Key'
openai_key = 'OPEN AI API KEY'
BOT_STATE = {'all': 'Default'}
client = OpenAI(
    api_key=openai_key,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    await update.message.reply_text("Hello, I'm AI Send Chat 🤖.")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(
        f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'Default'


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    await update.message.reply_text("I'm AI Send Chat 🤖\n"
                                    "Ask me anything related to the project and web3.\n"
                                    "I can process text/voice/video messages, analyze smart contracts, generate "
                                    "images and fetch realtime token data. \n\n"

                                    "/help - How to use the Bot❓\n"
                                    "/x - Answer questions 🤖\n"
                                    "/image - Generate image 🎨\n"
                                    "/ximage - Process the image 🔄🖼️\n"
                                    "/etherscan - Smart contract analysis 🔍📜🔒\n")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(
        f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'Default'


async def x_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    await update.message.reply_text('What is your question?')
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'Default'


async def image_gen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    await update.message.reply_text("Send the image description is the next message, e.g. 'cat'")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'IMAGE_GEN'


async def image_process_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = 'Please send me an image and your question as a caption.'  # update.message.text
    await update.message.reply_text(response)
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'IMAGE_PROCESS'


async def scan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    response = 'What is the address of the smart contract you want to analyze?'  # update.message.text
    await update.message.reply_text(response)
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'SCAN'


def bjson(msg):
    # parsed_json = json.loads(msg)
    beautiful_json = json.dumps(msg, indent=4)
    return beautiful_json


def split_string(text, limit):
    if len(text) <= limit:
        return [text]

    parts = []
    while len(text) > limit:
        part, text = text[:limit], text[limit:]
        parts.append(part)
    if text:
        parts.append(text)

    return parts


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def handle_responses(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there'

    elif 'hi' in processed:
        return 'Hey there'

    elif 'your creator' in processed:
        return 'My Creator and developer name is ABDULLAH AHMAD\n' \
               'You Can Contact him +92 315 0490481\n' \
               'Whatsapp: wa.me/923150490481'
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": processed},
            ]
        )
        return str(response.choices[0].message.content)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if BOT_STATE[update.message.chat.id] == 'IMAGE_GEN':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('img')
        await update.message.reply_text("Wait to generate image")
        msg = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')
        response = client.images.generate(
            model="dall-e-3",
            prompt=msg,
            size="1024x1024",
            n=1,
        )
        image_url = response.data[0].url
        img_data = requests.get(image_url).content
        r = random.randint(1, 100000000000000000000000000000000000)
        with open(f'{r}.png', 'wb') as handler:
            handler.write(img_data)
        chat_id = update.effective_chat.id
        print(image_url)
        # await update.message.reply_text(f"Image URL: {image_url}")
        await context.bot.send_photo(chat_id=chat_id, photo=open(f'{r}.png', 'rb'))
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    elif BOT_STATE[update.message.chat.id] == 'IMAGE_PROCESS':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('img process')
        msg = update.message.caption
        print(msg)
        r = random.randint(1, 100000000000000000000000000000000000)
        file = await update.message.photo[-1].get_file()
        path = await file.download_to_drive(f"Send-{r}.jpg")
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')
        base64_image = encode_image(path)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": msg},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=300
        )
        text = str(response.choices[0].message.content)
        await update.message.reply_text(text)
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    elif BOT_STATE[update.message.chat.id] == 'SCAN':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('scan')
        contract_address = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{contract_address}"')

        es = etherscan.Client(
            api_key=ETHSCAN,
            cache_expire_after=5,
        )
        eth_price = es.get_eth_price()
        eth_supply = es.get_eth_supply()
        eth_balance = es.get_eth_balance(contract_address)
        gas_price = es.get_gas_price()
        msg = f"Analyze it 'Analyzing smart contract at address: {contract_address}\n\n" \
              f"ETH Price: {eth_price}\n\n" \
              f"ETH Balance: {eth_balance}\n\n" \
              f"ETH Supply: {eth_supply}\n\n" \
              f"Gas Price: {gas_price}\n\n'"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": msg},
            ]
        )
        await update.message.reply_text(str(response.choices[0].message.content))
        print(f'Bot To: {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}', str(response.choices[0].message.content))
    else:
        print('msg')
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

        if message_type == 'group':
            if BOT_USERNAME in text:
                new_text: str = text.replace(BOT_USERNAME, 'AI Send Chat Bot').strip()
                response: str = handle_responses(new_text)
            else:
                return
        else:
            response: str = handle_responses(text)

        print('Bot:', response)
        await update.message.reply_text(response)
    print('out')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    print(
        f'{update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: Update {update} caused error {context.error}')
    await update.message.reply_text(str(context.error))


if __name__ == '__main__':
    print('STARTING BOT...')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('x', x_command))
    app.add_handler(CommandHandler('image', image_gen_command))
    app.add_handler(CommandHandler('ximage', image_process_command))
    app.add_handler(CommandHandler('etherscan', scan_command))

    # MESSAGES
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    # ERRORS
    app.add_error_handler(error)

    print('POLLING...')
    app.run_polling(poll_interval=1)
