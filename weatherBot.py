import discord, time, requests, os, json
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()


#gotta figure out userInput so the city isn't manual
cityName = "Toronto,CA"
APIKEY = os.getenv("APIKEY")
TOKEN = os.getenv("TOKEN")

#getTemp method uses the api to get the temp
def getTemp(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    temp = int(info['main']['temp'] -273.15)

    tempString = info['weather'][0]
    print(tempString)
    print(type(tempString))
    print(tempString['description'])
    return temp

#getWeather method uses the api to get the weather description
def getWeather(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()

    tempDic = info['weather'][0]
    desc = tempDic['description']

    return desc


# Create discord bot and set command prefix
bot = commands.Bot(command_prefix='!')

#create weather command
@bot.command(name='weather') 
async def weather(context):
    city = cityName
    y = str(getTemp(city,APIKEY))
    z = getWeather(city,APIKEY)
    x = y + "°" + " with " + z
    myEmbed = discord.Embed(title="Weather",description=x)
    
    await context.message.channel.send(embed=myEmbed)


@bot.command(name='commands')
async def help(context):
    x = "Command displays the temperature of a given city in celcius\n!weather [CITY][COUNTRY ABREVIATION]"
    myEmbed = discord.Embed(title="!weather",description=x)
    
    await context.message.channel.send(embed=myEmbed)

# Run bot
bot.run(TOKEN)


