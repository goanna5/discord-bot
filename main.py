# adapted from https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
import discord
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
intents.messages = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.author.name == client.user:
        return
    
    if message.content.lower() in ['hello','hi', 'hello goanna', 'hi goanna'] and message.author.name == "_goanna":
        await message.channel.send('Hello, my good-natured and benevolent mother')
    elif message.content.lower() in ['hello','hi', 'hello goanna', 'hi goanna']:
        await message.channel.send('Hello peasant')

    if 'goanna' in message.content.lower() and message.author.name != 'a solitary goanna':
        await message.channel.send('You summoned the goanna\nRAHHHHHHH\n🦎🦎🦎🦎🦎🦎🦎🦎')




print("Token from environment variable:", os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))