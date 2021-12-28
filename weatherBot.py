import discord, requests, os
from discord.ext import commands

from dotenv import load_dotenv
from requests.api import get
load_dotenv()


#call the apikey and token in to weatherBot.py
APIKEY = os.getenv("APIKEY")
TOKEN = os.getenv("TOKEN")

#getTemp method uses the api to get the temp
def getTemp(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    temp = int(info['main']['temp'] -273.15)
    
    return temp

#getWeather method uses the api to get the weather description
def getWeather(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    tempDic = info['weather'][0]
    desc = tempDic['description']
    return desc

#gets the icon code for the emoji and returns the url
def getEmoji(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    tempDic = info['weather'][0]
    weather_icon = tempDic['icon']
    url = "http://openweathermap.org/img/wn/" + weather_icon + "@2x.png"

    return url

#gets and returns the "feels like" temp
def getFeel(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    temp = int(info['main']['feels_like'] -273.15)
    
    return temp

#gets and returns the humidity 
def getHumidity(cityName,apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    info = requests.get(url).json()
    temp = int(info['main']['humidity'])
    
    return temp

# Create discord bot and set command prefix
bot = commands.Bot(command_prefix='!', help_command=None)

#create weather command
@bot.command(name='weather') 
async def weather(ctx, arg):

    #user enters a city
    city = arg
    #call the getEmoji function
    emoji = getEmoji(city,APIKEY)
    #call the getHumidity function and cast to string
    humidity = str(getHumidity(city,APIKEY)) + "%"
    #call the getFeel function and cast to string
    feel = str(getFeel(city,APIKEY)) + "°" 
    #call the getTemp function and cast to string
    y = str(getTemp(city,APIKEY))
    #call the getWeather function
    z = (getWeather(city,APIKEY))
    #weather description
    x = y + "°" + " with " + z 

    #embedded message with all the information gathered
    myEmbed = discord.Embed(title="Weather in " + city.upper(),description=x)
    myEmbed.set_author(name="Weather Bot")
    myEmbed.set_thumbnail(url=emoji)
    myEmbed.add_field(name='Humidity',value=humidity,inline=True)
    myEmbed.add_field(name='Feels Like',value=feel,inline=True)

    #send to the channel
    await ctx.message.channel.send(embed=myEmbed)


#instructions on how to properly use the bot
@bot.command(name='help')
async def help(ctx):
    x = "!weather [CITY][COUNTRY ABREVIATION]"
    y = "!weather [CITY]"
    z = '!weather "[CITY][COUNTRY ABREVIATION]"'
    a = '!weather "[CITY]"'
    myEmbed = discord.Embed(title="Weather Bot",description=x)
    myEmbed.add_field(name="or",value=y,inline=True)
    myEmbed.add_field(name="or",value=z,inline=False)
    myEmbed.add_field(name="or",value=a,inline=False)
    
    await ctx.message.channel.send(embed=myEmbed)


#error message
@weather.error
async def error(ctx,error):
     await ctx.message.channel.send('Try the "!help" command')

# Run bot
bot.run(TOKEN)