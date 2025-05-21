# Simple Python Telegram Bot Package

This homework project involves creating a basic Python package for interacting with the Telegram Bot API. The focus is on implementing core functionality like receiving updates and sending messages.

## Tasks

### 1. Project Setup (30 points)
- Create the basic project structure with the following files:
  ```
  python-telegram-bot/
  ├── src/
  │   ├── simple_telegram_bot/
  │   │   ├── __init__.py
  │   │   ├── bot.py
  │   │   └── api.py
  │   └── setup.py
  ├── requirements.txt
  └── README.md
  ```
- Initialize a virtual environment
- Set up `requirements.txt` with necessary dependencies (requests)
- Create a proper `setup.py` for package installation

### 2. Core Bot Implementation (40 points)

#### Task 2.1: Basic Bot Class
In `bot.py`, implement a `TelegramBot` class with:
- Initialize with bot token
- Method to get bot information
- Method to get updates
- Method to send text messages

Example structure:
```python
class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"

    def get_me(self):
        """Get basic information about the bot"""
        pass

    def get_updates(self, offset: int = None):
        """Get updates from Telegram"""
        pass

    def send_message(self, chat_id: int, text: str):
        """Send a text message"""
        pass
```

#### Task 2.2: API Handler
In `api.py`, implement basic HTTP methods for interacting with Telegram API:
- GET requests
- POST requests
- Error handling

### 3. Testing (30 points)
Create a simple example script that:
- Creates a bot instance
- Gets updates in a loop
- Responds to "/start" command with a welcome message
- Echoes back any text message received

## Requirements
1. Use only the `requests` library for HTTP requests (no external telegram libraries)
2. Implement proper error handling
3. Add basic documentation for each method
4. Follow PEP 8 style guidelines

## Bonus Points (20 points)
- Implement message formatting (bold, italic, etc.)
- Add support for sending photos
- Implement a simple command handler system

## Getting Started
1. Create a new bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Set up the project structure
4. Implement the required functionality
5. Test your implementation

## Evaluation Criteria
- Code quality and organization (20%)
- Implementation of required features (40%)
- Error handling (20%)
- Documentation (20%)

## Submission
- Submit your code as a GitHub repository
- Include requirements.txt
- Add example usage in README.md
- Provide test cases demonstrating the functionality