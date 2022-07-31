import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
import aiosqlite


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '$', intents=intents)

#Check if bot is on
@client.event
async def on_ready():
    print("Logged in as: {0.user}".format(client))
    async with aiosqlite.connect("gear.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute('CREATE TABLE IF NOT EXISTS gear (id INTEGER, guild INTEGER)')
        await db.commit()


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

#



# Client Token:
client.run(os.environ["DISCORD_TOKEN"])
#client.run('MTAwMzAwNDMzODg3NDEwNjA0Ng.Gfnx24.52sk9eHSvhBvOfWEt8V1M3EFcgP8S7cVmFAhe0')