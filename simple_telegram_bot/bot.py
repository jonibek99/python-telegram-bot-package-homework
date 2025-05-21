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

    def send_photo(
        self, chat_id: Union[int, str], photo: str, caption: Optional[str] = None
    ) -> Dict:
        """Send a photo message.

        Args:
            chat_id (Union[int, str]): Chat ID to send photo to
            photo (str): File path or URL of the photo
            caption (str, optional): Caption for the photo

        Returns:
            Dict: Message information
        """
        params = {"chat_id": chat_id, "photo": photo}
        if caption:
            params["caption"] = caption
        response = requests.post(f"{self.base_url}/sendPhoto", json=params)
        return response.json()

    def send_document(
        self, chat_id: Union[int, str], document: str, caption: Optional[str] = None
    ) -> Dict:
        """Send a document.

        Args:
            chat_id (Union[int, str]): Chat ID to send document to
            document (str): File path or URL of the document
            caption (str, optional): Caption for the document

        Returns:
            Dict: Message information
        """
        params = {"chat_id": chat_id, "document": document}
        if caption:
            params["caption"] = caption
        response = requests.post(f"{self.base_url}/sendDocument", json=params)
        return response.json()

    def send_audio(
        self, chat_id: Union[int, str], audio: str, caption: Optional[str] = None
    ) -> Dict:
        """Send an audio file.

        Args:
            chat_id (Union[int, str]): Chat ID to send audio to
            audio (str): File path or URL of the audio file
            caption (str, optional): Caption for the audio

        Returns:
            Dict: Message information
        """
        params = {"chat_id": chat_id, "audio": audio}
        if caption:
            params["caption"] = caption
        response = requests.post(f"{self.base_url}/sendAudio", json=params)
        return response.json()

    def send_dice(self, chat_id: Union[int, str], emoji: Optional[str] = None) -> Dict:
        """Send a dice message.

        Args:
            chat_id (Union[int, str]): Chat ID to send dice to
            emoji (str, optional): Emoji on which the dice throw animation is based.
                                 Currently, must be one of "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰"

        Returns:
            Dict: Message information
        """
        params = {"chat_id": chat_id}
        if emoji:
            params["emoji"] = emoji
        response = requests.post(f"{self.base_url}/sendDice", json=params)
        return response.json()
