import discord, time
from discord.ext import commands

# Create discord bot and set command prefix
bot = commands.Bot(command_prefix='!')

@bot.command(name='weather')
async def weather(context):
    myEmbed = discord.Embed(title="Weather",description="Bot Version 1.0")
    
    await context.message.channel.send(embed=myEmbed)

# Run bot
bot.run("OTIzNDk1NTk5MTE3MDc0NTAy.YcQ2TA.I3cdJpL6U0hlgK0dFcIIeN3lgmQ")


