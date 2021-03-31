import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_joim
@client.command()
async def ping(ctx):
    await ctx.send("pong")
@cliend.command()
async def kick(ctx, member : discord.Member,*, reason = None):
    await member.kick(reason = reason)
@cliend.command()
async def ban(ctx, member : discord.Member,*, reason = None):
    await member.ban(reason = reason)
    





client.run('ODI2ODYzMTY2Nzk2NDY0MTU4.YGSqVQ.G_kZIALjydMikNNmvy5USkuR0Q8')