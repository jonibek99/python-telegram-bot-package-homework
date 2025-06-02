import requests


class TelegramBot:
    def __init__(self, token):
        """Initialize the bot with the given token.

        Args:
            token: The Telegram Bot API token from BotFather
        """
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"

    def get_me(self):
        """Get basic information about the bot.

        Returns:
            Dictionary containing bot information (id, username, name)
        """
        response=requests.get(f"{self.base_url}/getMe")
        return(response.json())

    def get_updates(self, offset=None):
        """Get updates from Telegram.

        Args:
            offset: Message offset ID to start from (optional)

        Returns:
            List of update objects from Telegram
        """
        params={}
        if offset!=None:
            params['offset']=offset
        res=requests.get(f'{self.base_url}/getUpdates',params=params)
        return(res.json()['result'])

    def send_message(self, chat_id, text):
        """Send a text message.

        Args:
            chat_id: Chat ID to send message to
            text: Message text to send

        Returns:
            Dictionary containing sent message information
        """
        re=requests.post(f'{self.base_url}/sendMessage',params={'chat_id':chat_id,'text':text})
        return(re.json())

    def send_photo(self, chat_id, photo, caption=None):
        """Send a photo message.

        Args:
            chat_id: Chat ID to send photo to
            photo: File path or URL of the photo
            caption: Caption for the photo (optional)

        Returns:
            Dictionary containing sent message information
        """
        re=requests.post(f'{self.base_url}/sendPhoto',params={
            'chat_id':chat_id,
            'photo':photo,
            'caption':caption,

        })
        return re.json()

    def send_document(self, chat_id, document, caption=None):
        """Send a document.

        Args:
            chat_id: Chat ID to send document to
            document: File path or URL of the document
            caption: Caption for the document (optional)

        Returns:
            Dictionary containing sent message information
        """
        params={
            'chat_id':chat_id,
            'document':document,
            'caption':caption
        }
        re=requests.post(f'{self.base_url}/sendDocument',params=params)
        return re.json()

    def send_audio(self, chat_id, audio, caption=None):
        """Send an audio file.

        Args:
            chat_id: Chat ID to send audio to
            audio: File path or URL of the audio file
            caption: Caption for the audio (optional)

        Returns:
            Dictionary containing sent message information
        """
        params={
            'chat_id':chat_id,
            'audio':audio,
            'caption':caption
        }
        re=requests.post(f'{self.base_url}/sendAudio',params=params)
        return re.json()

    def send_dice(self, chat_id, emoji=None):
        """Send a dice message.

        Args:
            chat_id: Chat ID to send dice to
            emoji: Emoji for the dice animation (optional)
                  Can be "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰"

        Returns:
            Dictionary containing sent message information
        """
        params={
            'chat_id':chat_id,
            'emoji':emoji,
        }
        re=requests.post(f'{self.base_url}/sendDice',params=params)
        return re.json()