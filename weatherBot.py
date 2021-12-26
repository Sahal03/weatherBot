import discord, time, requests, os
from discord.ext import commands
    
cityName = "Toronto,CA"
APIKEY = "123128677fc96baa97b563b3e09e4731"
TOKEN = "OTIzNDk1NTk5MTE3MDc0NTAy.YcQ2TA.x9cTvq__-kzf-rwV51UzwfCuYxY"

def getWeather(cityName,apiKey):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
        info = requests.get(url).json()
        temp = int(info['main']['temp'] -273.15)
        return temp
    



# Create discord bot and set command prefix
bot = commands.Bot(command_prefix='!')

#create weather command
@bot.command(name='weather') 
async def getCity():
        msg = await bot.wait_for("weather", check=requests.check_compatibility)
        return msg
async def weather(context):
    city = getCity()
    y = str(getWeather(city,APIKEY))
    x = y + "°"
    myEmbed = discord.Embed(title="Weather",description=x)
    
    await context.message.channel.send(embed=myEmbed)

@bot.command(name='commands')
async def help(context):
    x = "Command displays the temperature of a given city in celcius\n!weather [CITY][COUNTRY ABREVIATION]"
    myEmbed = discord.Embed(title="!weather",description=x)
    
    await context.message.channel.send(embed=myEmbed)

# Run bot
bot.run(TOKEN)


