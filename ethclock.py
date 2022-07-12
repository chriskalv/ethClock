##################################
############ ETHCLOCK ############
############## BY CK #############
##################################

# --------------------------------
# --------Global Settings---------
# Etherscan API data:
etherscanAPI = "your etherscan.io API key"
# OpenWeather API data:
owmAPI = "your openweathermap.org API"
latitude = "99.9999"
longitude = "99.9999"
# Locale
tempscale = "metric"  # use either "metric" for °C or "imperial" for °F
language = "english" # use either "english", "german", "spanish" or "french" for the display of weekdays in the corresponding language
# --------------------------------

# Libraries and global variables for...
# ...clock functionality
import time
from threading import Thread
current_time = "25:61"
current_date = "00.00.0000"
# ...API requests
import requests
import json
current_weekdaytemp = "Keintag, 99°C"
blockdisplay = "ETH Block 000000000"
# ...display functionality
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(dispwidth, dispheight, board.I2C(), addr=0x3d, reset=digitalio.DigitalInOut(board.D4))
dispwidth = 128
dispheight = 64

# Load fonts
font = ImageFont.truetype('data-latin_mod.ttf', 28)
font1 = ImageFont.truetype('data-latin_mod.ttf', 12)
font2 = ImageFont.truetype('data-latin_mod.ttf', 10)

# Establish locale for days of the week
if language = "german":
    weekdays = ("Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag")
elif language = "spanish":
    weekdays = ("Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado")
elif language = "french":
    weekdays = ("Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi")
else:
    weekdays = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
# Establish locale for temperature scale       
if tempscale = "imperial":
    tempunit = "°F"
else:
    tempunit = "°C"

# Clear display and wait a second
oled.fill(0)
oled.show()
time.sleep(1)

# Function for creating a string that shows the current height of the ethereum blockchain
def blockheight():
    # Load global variables
    global blockdisplay
    
    # Get current time in UNIX timestamp as integer
    current_timeUNIX = int(time.time())
    
    # Generate Etherscan API URL and request the block height of the current UNIX timestamp
    etherscanRequest = requests.get("https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=" + str(current_timeUNIX) + "&closest=before&apikey=" + etherscanAPI).text

    # Load JSON from API request, search for block height and create displayable string
    response_info = json.loads(etherscanRequest)
    blockheight = response_info['result']
    blockdisplay = "ETH Block " + blockheight

# Create and start an individual loop to execute blockheight() every 25 seconds
def startblockloop():
    while True:
        blockheight()
        time.sleep(25)        
Thread(target=startblockloop).start()

# Function for creating a string that shows the current temperature in a defined area by usage of the OpenWeatherMap API
def tempdate():
    # Load global variables
    global current_date
    global current_weekdaytemp
    
    # Get weather data (temperature) by requesting OpenWeatherMap API for geographical data (Alter Lether Weg 6, Halen)    
    owmRequest = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid=" + owmAPI + "&units=" + tempscale)
      
    if owmRequest.status_code == 200:
        data = owmRequest.json()
        main = data['main']
        temp = int(main['temp'])
    
    # Get/set current date and day of the week (by conversion)
    current_weekdaynumber = int(time.strftime("%w"))        
    current_weekdaytemp = weekdays[current_weekdaynumber] + ", " + str(temp) + tempunit
    current_date = time.strftime("%d.%m.%Y")
        
# Create and start an individual loop to execute tempdate() every minute
def starttemploop():
    while True:
        tempdate()
        time.sleep(60)        
Thread(target=starttemploop).start()

# Function for creating strings that show time
def timescript():
    # Load global variables
    global current_time  
    
    # Get/set current 24h time
    current_time = time.strftime("%H:%M")

# Create and start an individual loop to execute timescript() every second
def starttimeloop():
    while True:
        timescript()
        time.sleep(1)        
Thread(target=starttimeloop).start()

# Give the environment some time
time.sleep(5)

# Function for passing previously gathered data to the display
def showdisplay():   
    # Create blank image for drawing
    image = Image.new("1", (dispwidth, dispheight))
    draw = ImageDraw.Draw(image)
        
    # Calculate sizes of strings on display
    widthtime, heighttime = draw.textsize(current_time, font = font)
    widthday, heightday = draw.textsize(current_weekdaytemp, font = font1)
    widthdate, heightdate = draw.textsize(current_date, font = font1)
    widthblock, heightblock = draw.textsize(blockdisplay, font = font2)
        
    # Draw time, date, weekday and block height
    draw.text(((dispwidth-widthtime)/2,-8), current_time, font = font, fill = 255)
    draw.text(((dispwidth-widthday)/2,25), current_weekdaytemp, font = font1, fill = 255)
    draw.text(((dispwidth-widthdate)/2,37 ), current_date, font = font1, fill = 255)
    draw.text(((dispwidth-widthblock)/2,54), blockdisplay, font = font2, fill = 255)
    
    # Display image
    oled.image(image)
    oled.show()

while True:
    showdisplay()
    time.sleep(1)
