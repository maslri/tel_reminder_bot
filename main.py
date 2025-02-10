from telethon.sync import TelegramClient, events
from constant import START_HALEP


api_id = 17349
api_hash = "344583e45741c457fe1862106095a5eb"
bot_token = "8192099591:AAHzNEnHdUIFky8GcAErvqqSQiLzqOeAzuM"
client = TelegramClient("wmt", api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern="/start"))
async def handler(event):
    await event.reply(START_HALEP)


client.run_until_disconnected()
