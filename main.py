# adapted from https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
# and https://dev.to/mannu/ 
# and https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py
import discord
import os
from dog import *
from ageify import *
from dotenv import load_dotenv
from discord import app_commands
load_dotenv()

intents = discord.Intents.all()
intents.messages = True
intents.presences = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# help
@tree.command(
    name="help",
    description="Will help you!!",
    guild=discord.Object(id=1160760529879584808)
)

async def help_command(interaction):
    await interaction.response.send_message("Help:\n\n**/ageify count||age"
                                            + "*name*** - will return number "
                                            + "of people with a certain name or the average "
                                            + "age of people with that name\n*e.g. /ageify count "
                                            + "Anna or /ageify age Anna*\n\n**/dog** "
                                            + "- will return a random dog picture from the dog "
                                            + "API\n\n**/help** - shows you this command as you know")

# ageify
@tree.command(
    name="ageify",
    description="Shows the number of people or average age of people with that name",
    guild=discord.Object(id=1160760529879584808)
)

@app_commands.describe(name="Enter a name",
                       option="What you want to see (count or age)")
async def ageify_command(interaction, option: str, name: str):
    if option in ["count", "age"]:
        await interaction.response.send_message(ageify(name, option))
    else:
        await interaction.response.send_message("Must specify either \"count\" or \"age\"" +
                                                " specifically in the option field")
        
# dog
@tree.command(
    name="dog",
    description="Cute dog pic anyone?",
    guild=discord.Object(id=1160760529879584808)
)

async def dog_command(interaction):
    await interaction.response.send_message(getDog())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    # await client.tree.sync()
    await tree.sync(guild=discord.Object(id=1160760529879584808))

# checking for greetings to respond to
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

print("Token from environment variable:", os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))