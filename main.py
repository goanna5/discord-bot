# adapted from https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
import discord
import os
from dog import *
from ageify import *
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
    if f"{message.author.name}#6841" == client.user:
        return
    
    hello_phrases = ['hello solitary goanna', 'hi solitary goanna', 
                     'hello a solitary goanna', 'hi a solitary goanna']
    
    if message.content.lower() in hello_phrases and message.author.name == "_goanna":
        await message.channel.send('Hello, my good-natured and benevolent mother')
    
    elif message.content.lower() in hello_phrases:
        await message.channel.send('Hello, peasant')

    elif 'goanna' in message.content.lower() and message.author.name != 'a solitary goanna':
        await message.channel.send('You summoned the goanna\nRAHHHHHHH\n🦎🦎🦎🦎🦎🦎🦎🦎')

    # API commands (note it starts with /g)
    if message.content.startswith('/g dog'):
        await message.channel.send(getDog())

    if message.content.lower().startswith('/g name'):
        # if in form '/g name Michael age' will return the average age of people w that name
        # if in form '/g name Michael count' will return the number of people with the name
        name = message.content.split(" ")[2]
        value = message.content.lower().split(" ")[3]
        if value in ["age\n", "count\n", "age", "count"]:
            await message.channel.send(ageify(name, value))
        else:
            await message.channel.send("Must specify either age or count. Type \"/g help\" to get more info")

    # help
    if message.content.lower().startswith('/g help'):
        await message.channel.send("Help:\n\n**/g name *your-name-goes-here* count||age** - " +
                                   "e.g. /g name Anna count  or  /g name Anna age\nWill return number of people with the name Anna " +
                                   "or the average age of people with the name Anna\n\n" +
                                   "**/g dog** - will return a random dog picture from the dog API")

print("Token from environment variable:", os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))