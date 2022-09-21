import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def hayes(ctx):
    await ctx.send( 'Food. You. Consume.')

client.run('MTAyMTYyMjI5NjE0NzkyNzEwMQ.GqLJzb.UYAuYYI8Exl4swrYxZRBrI6Knz0NBLd2x3CIWA')