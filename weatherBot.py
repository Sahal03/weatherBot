import discord

# Create discord client
bot = discord.Client()

@bot.event
async def on_ready():
#...

    gen = bot.get_channel(804427366859276340)

    await gen.send("How about this weather?")
# Run bot
bot.run("OTIzNDk1NTk5MTE3MDc0NTAy.YcQ2TA.2GjGyKaaRfV4notmRcnpZeJI3Bs")


