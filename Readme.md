# AI Send Chat Bot 🤖

Welcome to the **AI Send Chat Bot** project! This Telegram bot integrates various web3 features with OpenAI and Ethereum tools. It allows users to interact with the bot for various tasks like smart contract analysis, image generation, and more.

## Features

- **Smart Contract Analysis**: Analyze Ethereum smart contracts by providing a contract address.
- **Text/Voice/Video Processing**: Ask questions related to Web3 or any other topics and get responses powered by OpenAI's GPT models.
- **Image Generation**: Generate images based on textual descriptions using OpenAI's DALL·E model.
- **Image Processing**: Process images and provide related responses.
- **Real-Time Token Data**: Fetch real-time Ethereum token data and gas prices.

## Commands

- `/start`: Start the bot and receive a greeting.
- `/help`: Get help and see a list of available commands.
- `/x`: Ask the bot a question and get a response based on AI.
- `/image`: Generate an image based on a text description.
- `/ximage`: Process an image with a text caption.
- `/etherscan`: Analyze an Ethereum smart contract by providing its address.

## Installation

To run the bot locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/aisendchatbot.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
   - `TOKEN`: Your Telegram bot token (obtainable from @BotFather on Telegram).
   - `ETHSCAN`: Your Etherscan API key (sign up at [Etherscan](https://etherscan.io/)).
   - `openai_key`: Your OpenAI API key (sign up at [OpenAI](https://beta.openai.com/)).

4. **Run the bot**:
    ```bash
    python bot.py
    ```

## Bot Workflow

The bot is designed to handle different user commands and states:
1. **Start Command**: Greets the user and logs the message.
2. **Help Command**: Provides a description of available features.
3. **Question Command (`/x`)**: Prompts the user to ask a question, and returns an AI-generated response.
4. **Image Generation Command (`/image`)**: Prompts the user to describe an image, and generates an image using DALL·E.
5. **Image Processing Command (`/ximage`)**: Processes the image sent by the user along with a caption.
6. **Etherscan Command (`/etherscan`)**: Prompts the user for a smart contract address, analyzes it, and provides Ethereum-related data.

## Technologies Used

- **Python**: The main programming language.
- **Telegram Bot API**: For building the bot and handling user interactions.
- **OpenAI GPT-3.5/4**: For AI responses to user queries.
- **Etherscan API**: To interact with Ethereum blockchain data.
- **DALL·E**: For generating images based on user input.

## Contributing

Feel free to fork the repository and create pull requests with bug fixes or feature enhancements.

## License 
![MIT License](https://img.shields.io/badge/license-MIT-green)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
