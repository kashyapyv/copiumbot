from email import message
import discord
import logging
#TOKEN=MTAwMzAwNDMzODg3NDEwNjA0Ng.Gfnx24.52sk9eHSvhBvOfWEt8V1M3EFcgP8S7cVmFAhe0
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as: {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!cope'):
        await message.channel.send("Hello!")

client.run('MTAwMzAwNDMzODg3NDEwNjA0Ng.Gfnx24.52sk9eHSvhBvOfWEt8V1M3EFcgP8S7cVmFAhe0')