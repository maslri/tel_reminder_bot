from telethon.sync import TelegramClient, events
from utils import get_started_test
from databate import User
from datetime import datetime

api_id = 17349
api_hash = "344583e45741c457fe1862106095a5eb"
bot_token = "8192099591:AAHzNEnHdUIFky8GcAErvqqSQiLzqOeAzuM"
client = TelegramClient("wmt", api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern="/start"))
async def handler(event):
    sender = await event.get_sender()
    user_id = sender.id
    user_first_name = sender.first_name
    user_last_name = sender.last_name
    User.get_or_create(
        name=user_first_name + " " + user_last_name, user_id=user_id
    )
    await event.reply(get_started_test(user_first_name, user_last_name))


@client.on(events.NewMessage(pattern="/add"))
async def add_task(event):
    text = event.raw_text

    result = []
    for i in text.split("\n"):
        if len(i) > 0:
            result.append(i)
    title = result.pop(0).replace("/add", "").strip()
    date = datetime.strptime(result.pop(-1), "%Y:%m:%d %H:%M")
    description = "\n".join(result)

    await event.reply(
        f"Title: {title}\n\nDescription: {description}\n\nDate: {date}"
    )


client.run_until_disconnected()
