import requests
from typing import Optional, Dict, List, Union


class TelegramBot:
    def __init__(self, token: str):
        """Initialize the bot with the given token.

        Args:
            token (str): Telegram Bot API token obtained from BotFather
        """
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"

    def get_me(self) -> Dict:
        """Get basic information about the bot.

        Returns:
            Dict: Bot information including id, username, name
        """
        response = requests.get(f"{self.base_url}/getMe")
        return response.json()

    def get_updates(self, offset: Optional[int] = None) -> List[Dict]:
        """Get updates from Telegram.

        Args:
            offset (int, optional): Update ID to start from

        Returns:
            List[Dict]: List of update objects
        """
        params = {"offset": offset} if offset else {}
        response = requests.get(f"{self.base_url}/getUpdates", params=params)
        return response.json().get("result", [])

    def send_message(self, chat_id: Union[int, str], text: str) -> Dict:
        """Send a text message.

        Args:
            chat_id (Union[int, str]): Chat ID to send message to
            text (str): Message text to send

        Returns:
            Dict: Message information
        """
        params = {"chat_id": chat_id, "text": text}
        response = requests.post(f"{self.base_url}/sendMessage", json=params)
        return response.json()
