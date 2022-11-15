import telebot
from bs4 import BeautifulSoup
import requests
from datetime import date



API_KEY = ('5730661840:AAFm0l0b1LyjxFNK-bMKs7WhjBDCKFgcnsc') #telegram bot API KEY(TOKEN)
bot = telebot.TeleBot(API_KEY) #create bot
@bot.message_handler(commands=['weather']) #add command( /weather ) 

def weather(message): #function weather
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    user_input = str(message.text) #text coming from user( /weather CityName )
    city = user_input.replace('/weather','') #replace /weather with '' (CityName)
    
    today = str(date.today()) #today's date

    res = requests.get(f'https://www.google.com/search?q={city} weather&oq={city} weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    weather_status = soup.select('#wob_tm')[0].getText() #get weather status
    rain_probability = soup.select('#wob_pp')[0].getText() # get rain probability
    

    data = f'Date:{today} \n'\
        f'City:{city} \n'\
        f'Weather Status:{weather_status}C° \n'\
        f'Rain Probability:{rain_probability} '

    bot.send_message(message.chat.id,data) #gives the data to the user

@bot.message_handler(commands=['start']) #add command( /start ) 

def start(message): #start function
    bot.send_message(message.chat.id,'Hi! To use the bot /weather Baku(city name)')
    
bot.polling() #keep bot alive