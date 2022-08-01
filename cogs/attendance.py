from multiprocessing.connection import Client
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os
import requests

class attendance(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = "YES", style=nextcord.ButtonStyle.green)
    async def YES(self, button: nextcord.ui.button, interaction: Interaction):
        await interaction.response.send_message("Pressed YES", ephemeral=True)
        self.value = True 
    
    @nextcord.ui.button(label = "NO", style=nextcord.ButtonStyle.red)
    async def NO(self, button: nextcord.ui.button, interaction: Interaction):
        await interaction.response.send_message("Pressed NO", ephemeral=True)
        self.value = False
    
class UI(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    ServerID = [217633790690852864,496699147286609920]

    @nextcord.slash_command(name = "attendance", description="Button Test", guild_ids=ServerID)
    async def Attend(self, interaction: Interaction):
        view = attendance()
        await interaction.response.send_message("How does this work?", view=view)
        await view.wait()
        if view.value == None:
            return

        
def setup(client):
    client.add_cog(UI(client))