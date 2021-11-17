from Adafruit_IO import Client, RequestError, Feed
import time, serial
ADAFRUIT_IO_KEY = "aio_SDEv058Ml06emzp4bbZVKObVJgUw"
ADAFRUIT_IO_USERNAME = "Fer18313"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
feed1 = int
feed2 = int
serialcom2 = serial.Serial("COM2", baudrate = 9600, timeout = 1)
serialcom2.write(b"1")
while 1:
    try:
        feed1 = int(input("LAB5:"))
    except:
        exit()
    digital_feed1 = aio.feeds('LAB5')
    aio.send_data(digital_feed1.key, feed1)
    digital_data1 = aio.receive(digital_feed1.key)
    print(f'digital signal: {digital_data1.value}')
    #time.sleep(5)
    try: 
        feed2 = int(input("lab5_1:"))
    except:
        exit()
    digital_feed2 = aio.feeds('lab5_1')
    aio.send_data(digital_feed2.key, feed2)
    digital_data2 = aio.receive(digital_feed2.key)
    print(f'digital signal: {digital_data2.value}')