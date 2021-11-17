# CÃ³digo de ejemplo AdafruitIO
# Universidad del Valle de Guatemala
# IE3027 - ElectrÃ³nica Digital 2
# Diego Morales

# Adafruit IO
# https://io.adafruit.com/

# if Module not Found. Open Terminal/CMD and execute:
# pip3 install Adafruit_IO

from Adafruit_IO import Client, RequestError, Feed
import serial
import time
ADAFRUIT_IO_USERNAME = "Fernando18313"
ADAFRUIT_IO_KEY = "aio_HIvq37SzsC3TZ9XKEy5eN0I5o1IY"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Digital Feed

#port = serial.Serial("COM4",9600)
#port.timeout = 3
#time.sleep(1)
#print('PORT INITIALIZED CORRECTLY')

digitalfeed = aio.feeds("temperature")
digitalfeed2 = aio.feeds("humidity")
digitalfeed3 = aio.feeds("ldr")

aio.send_data(digitalfeed.key,33)
aio.send_data(digitalfeed2.key,51)
aio.send_data(digitalfeed3.key,70)
time.sleep(50)
aio.send_data(digitalfeed.key,36)
aio.send_data(digitalfeed2.key,58)
aio.send_data(digitalfeed3.key,35)