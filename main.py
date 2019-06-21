#!/bin/python3

from discord.ext import commands
import discord.utils
import discord
import json

client = discord.Client()
bot = commands.Bot(command_prefix='noops ', description='Discord hackweek meets noops...')

@bot.event
async def on_ready():
    print ('online')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def stats(ctx):
    """ Sends stats about Discord Noops """
    await ctx.send(
        "Mr FilloFluffy is in {} servers, serving {} users".format(
            len([i for i in bot.guilds]),  # servers
            len([i for i in bot.get_all_members()])  # members
        )
    )

@bot.command()
async def invite(ctx):
    """ sends invite link to bot """
    rl = 'https://discordapp.com/oauth2/authorize?client_id=591673432111054871&scope=bot&permissions=84992'
    msg = discord.Embed (
        title = 'Invite Link',
        description = 'Invite me to yer server with this >.<',
        image = bot.user.avatar_url,
        url = rl
    ).set_author(name = bot.user.name,url = rl, icon_url = bot.user.avatar_url )
    await ctx.send(embed=msg)

@bot.command()
async def credits(ctx):
    """ credits """
    await ctx.send("https://github.com/Mik1337/discord-noops \n https://github.com/Mik1337/fizzbot")

def loadCreds():
    with open('creds.json') as f:
        return json.load(f)

initial_extensions = [ "cogs.fizzbot",]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(loadCreds()['token'])
