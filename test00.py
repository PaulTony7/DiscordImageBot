import discord
import sys
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!paly'):
        await message.channel.send('Słocki zjebałeś!')

client.run(sys.argv[1])