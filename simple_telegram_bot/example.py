from bot import TelegramBot
import time


def main():
    # Replace with your bot token
    bot = TelegramBot('8045285503:AAGGplQLaXiGpuhPA2MV5kjx7cowGZVB0Mo')
    print(bot.get_me())

    print("Bot started...")
    last_update_id = 0

    while True:
        # Get updates from Telegram
        updates = bot.get_updates(offset=last_update_id)

        for update in updates:
            # Update the last update ID
            last_update_id = update["update_id"] + 1

            # Extract message information
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "")

            if not chat_id:
                continue

            # Handle /start command
            if text == "/start":
                bot.send_message(
                    chat_id, "Hello! I'm a simple echo bot. Send me any message!"
                )
            # Echo back any other message
            else:
                bot.send_message(chat_id, f"You said: {text}")

        # Sleep to prevent too many requests
        time.sleep(1)


if __name__ == "__main__":
    main()
