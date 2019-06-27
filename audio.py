#import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
#import Adafruit_BBIO.PWM as PWM
import time, math
from decimal import *

'''ADC.setup()
pin1="P9_38"
#odef sonido(pin1):
while True:
 reading = ADC.read(pin1)
 milivolts = reading*1800
# db=20*math.log10(milivolts)
 print(round(reading,5))
 time.sleep(0.5)
# a=input("Ingrese nivel ")
# PWM.start("P9_14",a)
# temp_c =(milivolts / 10.0)+143.70-273.15
# return(float(temp_c))
'''
GPIO.setup("P8_28",GPIO.IN)
while True: 
 print(GPIO.input("P8_28"))
 time.sleep(0.1)
