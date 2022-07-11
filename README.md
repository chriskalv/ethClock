ETHclock
========================

A digital clock showing the time, date, day of the week, local temperature **AND** the current block of the Ethereum blockchain.

The code is entirely python-based. The build is easy and solder-free.

[![](https://i.imgur.com/SM2zNi8.png?raw=true)](https://i.imgur.com/SM2zNi8.png)


## Hardware
+ [Raspberry Pi Zero 2 WH](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
+ [Adafruit monochrome 1.3" Display (Qwiic compatible)](https://www.adafruit.com/product/938)
+ [SparkFun Qwiic SHIM](https://www.sparkfun.com/products/15794)
+ [SparkFun Qwiic Cable](https://www.sparkfun.com/products/14427)

## Case
+ [GeeekPi Transparent Acrylic Case for Raspberry Pi Zero](https://smile.amazon.de/gp/product/B07MGFRHHR)
+ [Platic Hexagonal Spacers](https://smile.amazon.de/gp/product/B07CJGT93C?psc=1)


## Setup
1. Flash [Pi OS](https://www.raspberrypi.com/software/) onto the microSD card (SSH enabled), assemble the hardware and make the device connect to your WiFi.
2. `sudo apt-get update && sudo apt-get upgrade -y`
3. Install the Adafruit SSD1306 library in order for your display to work. You can find the Instructions [here](https://learn.adafruit.com/monochrome-oled-breakouts/python-setup)
4. Create the API key that is needed in order to show the current ETH block:
  1. Head over to [Etherscan.io](https://etherscan.io/) and create an account.
  2. Go to __[My Profile](https://etherscan.io/myaccount)__ --> __API Keys__ --> __Add +__  --> Enter a name and create the key.
5. Create the API key that is needed in order to display the current temperature:
  1. Head over to [OpenWeatherMap.org](https://openweathermap.org/) and create an account.
  2. Go to __[My API Keys](https://home.openweathermap.org/api_keys)__, enter a name below __Create Key__ and hit __Generate__.
  3. Make sure the __Status__ of the newly generated key is set to 'active'.
7. Copy the `ethclock.py` file to your device and edit the 'Global Settings' section of the script:
   - Paste your API keys from Etherscan and Openweather into the script
   - Make sure to edit permissions of files/folders, so the script can read, write and execute adequately (`sudo chmod 777 -R` your shazampi folder)
   - Make `ethclock.py` autostart on bootup
