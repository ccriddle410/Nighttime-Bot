import os
import discord
import asyncio
from keep_alive import keep_alive
import datetime
intents = discord.Intents(guilds=True, members=True)

client = discord.Client(intents=intents)
token = os.environ['token']
guild_id = os.environ['guild_id']
so_id = os.environ['so_id']
me_id = os.environ['me_id']
my_id = os.environ['my_id']

async def my_background_task():
    await client.wait_until_ready()

    guild = await client.fetch_guild(guild_id)
    so = await guild.fetch_member(so_id)
    me = await guild.fetch_member(me_id)
    my = await guild.fetch_member(my_id)   

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        day = datetime.datetime.today().weekday()

        # Sophie Block
        if hour >= 4 and hour <= 10 and day <= 4:
            try:
              await so.edit(mute=True)
              await so.edit(deafen=True)
              await so.edit(voice_channel=None)
            except:
              pass
        elif (hour < 4 or hour > 10) or day > 4:
          try: 
            await so.edit(mute=False)
            await so.edit(deafen=False)
          except:
              pass

        # Metze Block
        if hour >= 4 and hour <= 10 and day <= 4:
          try:
            await me.edit(mute=True)
            await me.edit(deafen=True)
            await me.edit(voice_channel=None)
          except:
              pass
        elif (hour < 4 or hour > 10) or day > 4:
          try:
            await me.edit(mute=False)
            await me.edit(deafen=False)
          except:
              pass

        # Mystic Block
        if hour >= 7 and hour <= 13 and day <= 4:
          try:
            await my.edit(mute=True)
            await my.edit(deafen=True)
            await my.edit(voice_channel=None)
          except:
              pass
        elif (hour < 7 or hour > 13) or day > 4:
          try:
            await my.edit(mute=False)
            await my.edit(deafen=False)
          except:
            pass

        await asyncio.sleep(10)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

keep_alive()
client.loop.create_task(my_background_task())
client.run(token)