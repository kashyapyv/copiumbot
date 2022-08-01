import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
import psycopg2


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '$', intents=intents)

conn = psycopg2.connect(host=os.environ['HOST_NAME'], database=os.environ['DATABASE'], user=os.environ['USER_NAME'], password=os.environ['PASS_WORD'])

#Check if bot is on
@client.event
async def on_ready():
    print("Logged in as: {0.user}".format(client))
    


ServerID = 217633790690852864

#1st slash command
@client.slash_command(name='hello', description='It just says helllo back',guild_ids=[ServerID])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("Hello")

#setting up cogs
initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs."+ filename[:-3])

if __name__ =='__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

# Client Token:
client.run(os.environ['DISCORD_TOKEN'])