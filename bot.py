import discord
from discord.ext import commands
import sympy
from sympy import symbols, Symbol,preview
import math
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.command()
async def ping(ctx):
    await ctx.send("pong")
@client.command()
@commands.is_owner()
async def kick(ctx, member : discord.Member,*, reason = None):
    await member.kick(reason = reason)

@client.command()
@commands.is_owner()
async def ban(ctx, member : discord.Member,*, reason = None):
    await member.ban(reason = reason)

@client.command()
@commands.is_owner()
async def unban(ctx,*, member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return

@client.command()
async def latex(ctx,*,latex):
    preview(latex, viewer='file', filename='a.png', euler=False)
    await ctx.send(file=discord.File('a.png'))
    

token = ""
client.run(token)
