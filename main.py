import discord
import os
from twython import Twython

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

client = discord.Client()

@client.event
async def on_ready():
    print('Ready as {0.user}'.format(client))

@client.event
async def on_message(message):
    content = message.content
    splt = content.split('|')

    if content.count('|') > 2:
        await message.channel.send('error')
        return

    if message.author == client.user:
        return
    
    if splt[0] == ('$hi'):
        await message.channel.send('Hello!')
    
    if splt[0] == ('$ping'):
        await message.channel.send(f'Pong! My ping is `{round(client.latency * 1000)}ms`')

    if splt[0] == ('$embed'):
        details = twitter.show_user(screen_name=splt[1])
        embed = discord.Embed(description=splt[2], color=0x1DA1F2)
        embed.set_author(name = '@'+splt[1], icon_url = details['profile_image_url'])
        embed.set_footer(text = 'Twitter  •  Today at 12:09 AM', icon_url = 'https://help.twitter.com/content/dam/help-twitter/brand/logo.png')
        await message.channel.send('@'+splt[1]+' has Tweeted!')
        await message.channel.send(embed=embed)

client.run('')