import discord

# Create discord client
bot = discord.Client()

@bot.event
async def on_ready():
#...
    #assign channel id
    gen = bot.get_channel(804427366859276340)

    #send generic weather message to gen
    await gen.send("How about this weather?")
# Run bot
bot.run("OTIzNDk1NTk5MTE3MDc0NTAy.YcQ2TA.2GjGyKaaRfV4notmRcnpZeJI3Bs")


