import discord
import os


TOKEN=input ("token:")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        mail=input ("message:")
        await message.channel.send(mail)


client.run(TOKEN)

