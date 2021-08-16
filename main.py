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

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id

  if message_id == 876933514069692516:
    # I have no idea what these next two lines are doing. Ugh.
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

    # print(payload.emoji.name)

    # The above statement is how I discovered through debugging that these emojis, which seem to be system agnostic, have no names. Their names are just the emojis themselves. Wild.

    if payload.emoji.name == '🔵':
      print('Blue Team added.')
      role = discord.utils.get(guild.roles, name = 'Blue Team')
    elif payload.emoji.name == '🔴':
      print('Red Team added.')
      role = discord.utils.get(guild.roles, name = 'Red Team')
    elif payload.emoji.name == '🟢':
      print('Green Team added.')
      role = discord.utils.get(guild.roles, name = 'Green Team')
    elif payload.emoji.name == '🟡':
      print('Yellow Team added.')
      role = discord.utils.get(guild.roles, name = 'Yellow Team')
    else:
      role = discord.utils.get(guild.roles, name = payload.emoji.name)

    if role is not None:
      member = payload.member
      if member is not None:
        await member.add_roles(role)
        print('Role added.')
      else:
        print('Member not found.')
    else:
      print('Role not found.')


@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id

  if message_id == 876933514069692516:
    # Again...no idea.
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

    if payload.emoji.name == '🔵':
      print('Blue Team removed.')
      role = discord.utils.get(guild.roles, name = 'Blue Team')
    elif payload.emoji.name == '🔴':
      print('Red Team removed.')
      role = discord.utils.get(guild.roles, name = 'Red Team')
    elif payload.emoji.name == '🟢':
      print('Green Team removed.')
      role = discord.utils.get(guild.roles, name = 'Green Team')
    elif payload.emoji.name == '🟡':
      print('Yellow Team removed.')
      role = discord.utils.get(guild.roles, name = 'Yellow Team')
    else:
      role = discord.utils.get(guild.roles, name = payload.emoji.name)

    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.remove_roles(role)
        print('Role removed.')
      else:
        print('Member not found.')
    else:
      print('Role not found.')

client.run(os.getenv('token'))