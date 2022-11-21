import discord
from discord import app_commands
import random
import csv
from settings import *

random.seed()

with open("Tables/wildmagic.csv", "r") as file:
    reader = csv.DictReader(file)
    table = []
    for row in reader:
        table.append(row.copy())
    
def roll():
    rolled = random.choice(table)
    result = rolled.get("Effect")
    return str(result)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$wild'):
        await message.channel.send(f"{message.author} created a surge of wild magic! {roll()}")

client.run(DISCORD_TOKEN)
