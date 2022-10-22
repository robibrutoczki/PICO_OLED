from machine import Pin, I2C # to use I2C
from ssd1306 import SSD1306_I2C # OLED driver
from time import sleep # To wait between refresh etc
import utime as time # Time
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests



# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'Wifi name goes here'
password = 'Your password goes here'
wlan.connect(ssid, password)
if wlan.active() == True :
    print('OK')




print("ETH GBP ")
r = urequests.get("https://www.bitstamp.net/api/v2/ticker/ethgbp") # API request from bitstamp

print(r.json()['last']) # get info from json
r.close()

# Let's get the current time from a server
print("THE TIME IS :")
b = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/London") # Server that returns the current GMT+0 time.
print(b.json()['date'] +" " + b.json()['time'])
b.close()

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) #choose pins on the Pico
oled = SSD1306_I2C(128, 64, i2c) # Screen size


while True:
      r = urequests.get("https://www.bitstamp.net/api/v2/ticker/ethgbp")
      btc = urequests.get("https://www.bitstamp.net/api/v2/ticker/btcgbp")
      b = urequests.get("http://date.jsontest.com")
      oled.text("BTC GBP:", 30, 0)
      oled.text((btc.json()['last']), 36, 24)
      oled.show()
      sleep(3)
      oled.fill(0)
      oled.text("ETH GBP:", 30, 0)
      oled.text((r.json()['last']), 36, 24)
      oled.show()
      sleep(3)
      oled.fill(0)
      oled.text('DATE AND TIME:', 15, 0)
      oled.text((b.json()['date'] ), 25, 24)
      oled.show()
      sleep(1)
      oled.fill(0)
      oled.text('DATE AND TIME:', 15, 0)
      oled.text((b.json()['time'] ), 20, 24)
      oled.show()
      sleep(1)
      oled.fill(0)
     
      
    
      
