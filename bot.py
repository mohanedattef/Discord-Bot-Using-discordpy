import os
import discord
from dotenv import load_dotenv
from random import randint

rlyrics = open('lyrics2.txt', encoding='utf-8')
lyrics=rlyrics.readlines()
lines=len(lyrics)
lastline = 0


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!marwan|!chaos'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!marwan':
        gottenline=randint(1,lines)
        sentmssg=lyrics[gottenline]
        sentmssg = sentmssg.replace("|", '\n')
        response ='{}'.format(message.author.mention) +"\n"+ sentmssg
        await message.channel.send(response)

    if message.content == '!chaos':
        gottenline=randint(1,lines)
        sentmssg=lyrics[gottenline]
        sentmssg = sentmssg.replace("|", '\n')
        response ="@everyone" +"\n"+ sentmssg
        await message.channel.send(response)

    
    if message.content == '!help':
        response ='{}'.format(message.author.mention) +"\n"+ "Use !marwan to get your lyrics "+"\n"+ "Use !chaos to annoy everyone"
        await message.channel.send(response)



    
client.run(TOKEN)

