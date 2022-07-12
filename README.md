ETHclock
========================

A digital table clock, built from a Raspberry Pi Zero, showing the 
  - time
  - date
  - day of the week
  - local temperature ***AND***
  - the current block of the Ethereum blockchain.

The code is entirely python-based and pulls time data from the internet, not from a RTC chip like in many other clock builds. Assembly of the device is really easy and even solder-free in case you have a Pi Zero **WH** model. 

<br></br>

| Finished clock (front)   | Finished clock (back)   |
| ------------- | -------------|
| [![](https://i.imgur.com/J0NngF4.png?raw=true)](https://i.imgur.com/J0NngF4.png.jpg)   |   [![](https://i.imgur.com/hw6ClAO.png?raw=true)](https://i.imgur.com/hw6ClAO.png)   |

<br></br>

## Hardware
+ [Raspberry Pi Zero 2 WH](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
+ [Adafruit Monochrome 1.3" Display (Qwiic-compatible)](https://www.adafruit.com/product/938)
+ [SparkFun Qwiic SHIM](https://www.sparkfun.com/products/15794)
+ [SparkFun Qwiic Cable](https://www.sparkfun.com/products/14427)
+ [MicroSD Card](https://www.westerndigital.com/products/memory-cards/sandisk-high-endurance-uhs-i-microsd#SDSQQNR-032G-GN6IA) (pretty much any will do)

## Setup
#### I. Data Preparation
1. Create the API key that is needed in order to request the current Ethereum block:
    1. Head over to [Etherscan.io](https://etherscan.io/) and create an account.
    2. Go to _[My Profile](https://etherscan.io/myaccount)_ --> _API Keys_ --> _Add_, then enter a name and create the key.
2. Create the API key that is needed in order to get the current temperature:
    1. Head over to [OpenWeatherMap.org](https://openweathermap.org/) and create an account.
    2. Go to _[My API Keys](https://home.openweathermap.org/api_keys)_, enter a name below _Create Key_ and hit _Generate_.
3. Convert the address, for which the temperature should be displayed, into longitude & latitude coordinates with help of [LatLong.net](https://www.latlong.net/convert-address-to-lat-long.html).

You will need to paste both API keys and the data for langitude and latitude into the `ethclock.py` script later on, so you might want to already paste them somewhere you can find them again.

#### II. Device Work
1. Flash [Pi OS](https://www.raspberrypi.com/software/) onto the microSD card (SSH enabled), assemble the hardware and make the device connect to your WiFi.
2. `sudo apt-get update && sudo apt-get upgrade -y`
3. Install the Adafruit SSD1306 library in order for your display to work. You can find the Instructions [here](https://learn.adafruit.com/monochrome-oled-breakouts/python-setup).
4. Create a new folder on the device and copy the font file `data-latin_mod.ttf` and the script `ethclock.py` into it.
5. Make sure to edit permissions of the newly created folder and its files, so the script can later read, write and execute adequately (`sudo chmod 777 -R /<yourdirectoryname>/` will do)
6. Edit the **Global Settings** section at the top of `ethclock.py`:
    1. Paste your API keys from Etherscan and Openweather as well as your longitude/latitude data into the script.
    2. Change the displayed locale and temperature scale to your liking.
7. Make `ethclock.py` autostart on boot. Some instructions on how this can be done are [here](https://transang.me/three-ways-to-create-a-startup-script-in-ubuntu/).
8. If you want to disable the green status LED on the Pi Zero board, which some people find annoying, you can find out how to do that in [this](https://www.cnx-software.com/2021/12/09/raspberry-pi-zero-2-w-power-consumption/) post.
   
## Case
+ [GeeekPi Transparent Acrylic Case for Raspberry Pi Zero](https://smile.amazon.de/gp/product/B07MGFRHHR)
+ [Platic Hexagonal Spacers](https://smile.amazon.de/gp/product/B07CJGT93C?psc=1)
+ [Copper CPU Cooler](https://smile.amazon.de/-/en/gp/product/B01BJ3S73S?psc=1)

 1. From the transparent acrylic case, cut off a little part with a Stanley knife in order to make room for the Qwiic SHIM breakout. 
 2. Place a metal cooler onto the CPU. Any cooler will do and I'm pretty sure you do not really need one for this build.
 3. Shape two plastic hexagonal spacers with a Stanley knife and mount them to the bottom case screws, so the device can stand properly.
 4. Attach the display with a little bit of hot glue. Be careful not to damage it.

Obviously, this is just how I did it. There are endless possibilities on how to make your ETHclock look. By now, I've built a few of these with several different displays using various stands, so please don't feel like you have to "go by the book" here.
