from simple_telegram_bot.bot import TelegramBot
import time


def main():
    # Replace with your bot token
    bot = TelegramBot("YOUR_BOT_TOKEN")

    print("Bot started...")
    last_update_id = None

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
