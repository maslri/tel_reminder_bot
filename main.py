from telethon.sync import TelegramClient, events
from utils import get_started_test
from databate import User, Task
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
    User.get_or_create(name=user_first_name + " " + user_last_name, user_id=user_id)
    await event.reply(get_started_test(user_first_name, user_last_name))


@client.on(events.NewMessage(pattern="/add"))
async def add_task(event):
    text = event.raw_text

    result = []
    for i in text.split("\n"):
        if len(i) > 0:
            result.append(i)
    title = result.pop(0).replace("/add", "", 1).strip()
    date = datetime.strptime(result.pop(-1), "%Y:%m:%d %H:%M")
    description = "\n".join(result)

    sender = await event.get_sender()
    task = Task.create(
        user=sender.id, title=title, description=description, datetime=date
    )
    response_test = f"the {title} is created whose ID is = {task}"
    await event.reply(response_test)


@client.on(events.NewMessage(pattern="/list"))
async def list_task(event):
    sender = await event.get_sender()
    tasks = Task.select().where(Task.user == sender.id, ~Task.is_done)
    response_text = []
    for task in tasks:
        response_text.append(f"Task id {task.id} => {task.title} - {task.datetime}\n\n")
    response_text.append(
        "for remove or update task use /remove or /update with task id fron of them example: /remove 1"
    )
    await event.reply("".join(response_text))


@client.on(events.NewMessage(pattern="/remove"))
async def remove_task(event):
    task_id = event.raw_text.replace("/remove", "", 1).strip()
    sender = await event.get_sender()
    task = Task.get(Task.user == sender.id, Task.id == task_id)
    task.delete_instance()
    await event.reply(f"Task id {task_id} is removed")


client.run_until_disconnected()
