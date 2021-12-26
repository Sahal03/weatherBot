import discord, time

# Create discord client
bot = discord.Client()

@bot.event
async def on_ready():
#...
    #assign channel id
    gen = bot.get_channel(804427366859276340)
    for _ in range(5):
    #send generic weather message to gen
        await gen.send("IT'S GON RAIN")
        time.sleep(5)
# Run bot
bot.run("OTIzNDk1NTk5MTE3MDc0NTAy.YcQ2TA.kXRniVYxy0PC_JH34JkSlkYqJfQ")


