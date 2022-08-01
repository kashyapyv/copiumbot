from cProfile import label
from multiprocessing.connection import Client
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import requests
import aiosqlite
import psycopg2
import sys


#TServer ID:
ServerID = [217633790690852864,496699147286609920]
conn = psycopg2.connect(host=os.environ['HOST_NAME'], database=os.environ['DATABASE'], user=os.environ['USER_NAME'], password=os.environ['PASS_WORD'])
'''  cur = conn.cursor()
        guild = interaction.guild.id
        try:
            gear_table_query = """CREATE TABLE GEAR_""" + str(guild) + """"(
            USER_ID VARCHAR(20) NOT NULL,
            AP INTEGER DEFAULT 0,
            AAP INTEGER DEFAULT 0,
            DP INTEGER DEFAULT 0
            CLASS VARCHAR(20) DEFAULT 'NOT SET',
            PRIMARY KEY(USER_ID)
            )
            """
            setup_table = cur.execute(gear_table_query)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn.closed == 0:
                table = "GEAR_"+str(guild)'''

#selection dropdown for class
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
    @nextcord.client.slash_command(name = "gear", guild_ids=ServerID)
    async def gear(self, interaction: Interaction):
        pass

    #class selection
    @gear.subcommand(name="class", description = "Select Main Class")
    async def mainclass(self, interaction: Interaction):
        cur = conn.cursor()
        guild = interaction.guild.id
        try:
            gear_table_query = """CREATE TABLE IF NOT EXISTS GEAR_""" + str(guild) + """(
            USER_ID VARCHAR(20) NOT NULL,
            AP INTEGER DEFAULT 0,
            AAP INTEGER DEFAULT 0,
            DP INTEGER DEFAULT 0,
            CLASS VARCHAR(20) DEFAULT 'NOT SET',
            PRIMARY KEY(USER_ID)
            )
            """
            setup_table = cur.execute(gear_table_query)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            if conn.closed == 0:
                table = "GEAR_"+str(guild)
        table = "GEAR_"+str(guild)
        view = DropdownView()
        await interaction.response.send_message("Select Class",view=view, ephemeral=True)
  
    '''#create table
    @gear.subcommand(name="createtable")
    async def createtable(self, interaction: Interaction):
        guild = interaction.guild.id
        cur = conn.cursor()
        try:
            gear_table_query = """CREATE TABLE GEAR_""" + str(guild) + """(
            USER_ID VARCHAR(20) NOT NULL,
            AP INTEGER DEFAULT 0,
            AAP INTEGER DEFAULT 0,
            DP INTEGER DEFAULT 0,
            CLASS VARCHAR(20) DEFAULT 'NOT SET',
            PRIMARY KEY(USER_ID)
            )
            """
            setup_table = cur.execute(gear_table_query)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn.closed == 0:
                table = "GEAR_"+str(guild)
        await interaction.response.send_message(f"Table created for {guild}")'''
   
   
   
   
    #create command
    @gear.subcommand(name="new", description= "Use this for the first time: ")
    async def newg(self, interaction: Interaction,ap:int=SlashOption(required=False,default=0), aap:int=SlashOption(required=False,default=0), dp:int=SlashOption(required=False,default=0)):
        cur = conn.cursor()
        guild = interaction.guild.id
        table = "GEAR_"+str(guild)
        try:
                new_query = "INSERT INTO "+table+" (USER_ID,AP, AAP, DP) VALUES(%s,%s,%s,%s)"
                new_values = (str(interaction.user),ap,aap,dp,)
                cur.execute(new_query,new_values)
                conn.commit()
                cur.close()
        except BaseException as e:
            print(e)
            conn.rollback()
        await interaction.response.send_message(f"Gear set AP:{ap} AAP:{aap} DP:{dp}")
    
    
    
    
    #update command
    @gear.subcommand(name="update", description= "Update new gear values: ")
    async def update(self, interaction: Interaction,ap:int=SlashOption(required=False,default=0), aap:int=SlashOption(required=False,default=0), dp:int=SlashOption(required=False,default=0)):
        cur = conn.cursor()
        guild = interaction.guild.id
        table = "GEAR_"+str(guild)
        check_query_result = cur.execute(("SELECT USER_ID FROM "+table+" WHERE USER_ID=%s"), (str(interaction.user),))
        print(f"check query result = {check_query_result}") 
        try:
            select_query = """SELECT * FROM """+table+""" WHERE USER_ID=%s"""
            select_values = (str(interaction.user),)
            cur.execute(select_query, select_values)
            record = cur.fetchall()
            for row in record:
                old_ap = row[1]
                old_aap = row[2]
                old_dp = row[3]
            if ap == 0:
                ap = old_ap
            if dp == 0:
                dp = old_dp
            if aap == 0:
                aap = old_aap
            update_query = "UPDATE "+table+" SET AP = %s, AAP=%s, DP=%s WHERE USER_ID=%s"
            update_values = (ap,aap,dp,str(interaction.user),)
            cur.execute(update_query,update_values)
            conn.commit()
            cur.close()
        except BaseException as e:
            print(e)
            conn.rollback()
        '''else:
            try:
                new_query = "INSERT INTO "+table+" (USER_ID,AP, AAP, DP) VALUES(%s,%s,%s,%s)"
                new_values = (str(interaction.user),ap,aap,dp,)
                cur.execute(new_query,new_values)
                conn.commit()
                cur.close()
            except BaseException as e:
                print(e)
                conn.rollback()'''
        await interaction.response.send_message(f"Updated: {ap} AAP:{aap} DP:{dp}")






#Setup client
def setup(client):
    client.add_cog(gear(client))
  