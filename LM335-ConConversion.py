import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time, math
from decimal import *

	#utilizando GPIO
#GPIO.setup("P9_23", GPIO.IN) #pin 23 es una entrada beagle, lee la senal digital
#GPIO.setup("P9_25", GPIO.OUT) #pin 25 salida beagle alimenta led

#GPIO.output("P9_25", 1) #prende led
#time.sleep(5)
#GPIO.output("P9_25", 0) #apaga led

#utilizando ADC (analogo)
ADC.setup()
analogPin="P9_39"
suma0,suma=0,0
N=100


def steinhart_temperature_C(r, Ro=10.0, To=25.0, beta=3120.0):
  steinhart = math.log(r / Ro) / beta      # log(R/Ro) / beta
  steinhart += 1.0 / (To + 273.15)         # log(R/Ro) / beta + 1/To
  steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C
  return steinhart

for i in range(N):
#   GPIO.output("P9_25",1)
   thermistor=ADC.read(analogPin) #*3.42*1000
   R = 10000 / (1/thermistor - 1)
   t=round(steinhart_temperature_C(R),2)
   #s.append(soundVal)   #Creando una lsita
  # soundVol
   #print(thermistor,R)
   suma+=t
   time.sleep(0.1)
   print(t)
print("Promedio: "+str(suma/N))
