from cProfile import label
from multiprocessing.connection import Client
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import requests
import aiosqlite

#TServer ID:
ServerID = 217633790690852864

class mainclass(nextcord.ui.Select):
    def __init__(self):
        selectoptions =[
            nextcord.SelectOption(label="Archer"),
            nextcord.SelectOption(label="Berserker"),
            nextcord.SelectOption(label="Corsair"),
            nextcord.SelectOption(label="Dark Knight"),
            nextcord.SelectOption(label="Drakania"),
            nextcord.SelectOption(label="Guardian"),
            nextcord.SelectOption(label="Hashashin"),
            nextcord.SelectOption(label="Kunoichi"),
            nextcord.SelectOption(label="Maehwa"),
            nextcord.SelectOption(label="Musa"),
            nextcord.SelectOption(label="Mystic"),
            nextcord.SelectOption(label="Ninja"),
            nextcord.SelectOption(label="Nova"),
            nextcord.SelectOption(label="Ranger"),
            nextcord.SelectOption(label="Sage"),
            nextcord.SelectOption(label="Shai"),
            nextcord.SelectOption(label="Sorceress"),
            nextcord.SelectOption(label="Striker"),
            nextcord.SelectOption(label="Tamer"),
            nextcord.SelectOption(label="valkyrie"),
            nextcord.SelectOption(label="Warrior"),
            nextcord.SelectOption(label="Witch"),
            nextcord.SelectOption(label="Wizard")
        ]
        super().__init__(placeholder= "Select Main Class",min_values=1, max_values=1, options=selectoptions)

    async def callback(self, interaction: Interaction):
        if self.values[0] == "Archer":
            return await interaction.response.send_message("Oh no griefing yourself")
        await interaction.response.send_message(f'Selected:{self.values[0]}') 

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(mainclass())




class gear(commands.Cog):
    def __init__(self, client):
        self.client=client
        
    #slash command??
    @nextcord.client.slash_command(name = "gear", guild_ids=[ServerID])
    async def gear(self, interaction: Interaction):
        pass

    #class selection
    @gear.subcommand(name="class", description = "Select Main Class")
    async def mainclass(self, interaction: Interaction):
        view = DropdownView()
        await interaction.response.send_message("",view=view, ephemeral=True)
    #update command
    @gear.subcommand(name="update", description= "Update new gear values: ")
    async def update(self, interaction: Interaction,ap:int=SlashOption(required=False), aap:int=SlashOption(required=False), dp:int=SlashOption(required=False)):
        await interaction.response.send_message(f"You set AP: {ap} AAP:{aap} DP:{dp}")

#sqlite




#Setup client
def setup(client):
    client.add_cog(gear(client))
  