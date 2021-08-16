import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  # Checks for case sensitivity
  msg_check = message.content.lower()

  # Thorbot checks to see if message containing key words/phrases was sent by the program itself. If so, it simply returns nothing.
  if message.author == client.user:
    return

  # Thorbot then checks whether or not the message contains key words or phrases. If so, it executes the await code.
  if 'smart' in msg_check or 'safe' in msg_check:
    await message.channel.send('*"Play smafe."*')
  
  if 'cheese' in msg_check:
    await message.channel.send('https://imgur.com/a/r7lr7P4')

  if 'engram' in msg_check:
    await message.channel.send('https://imgur.com/a/e2RdpzT')

  if 'crota' in msg_check:
    await message.channel.send('Remember that time Banks scrapped his Hunger of Crota half-awake at 2:30AM?')

client.run(os.getenv('token'))