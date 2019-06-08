import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import os
import numpy as np
import matplotlib.pyplot as plt
from decimal import *

#utilizando GPIO
GPIO.setup("P9_23", GPIO.IN) #pin 23 es una entrada beagle, lee la senal digital
GPIO.setup("P9_25", GPIO.OUT) #pin 25 salida beagle alimenta led

#GPIO.output("P9_25", 1) #prende led
#time.sleep(5)
#GPIO.output("P9_25", 0) #apaga led

#utilizando ADC (analogo)
ADC.setup()
analogPin="P9_37"
while (1):
   GPIO.output("P9_25",1)
   soundVal=ADC.read(analogPin)
   soundVolt=soundVal*1.8*100
   print(GPIO.input("P9_23"),round(soundVolt,3))
   file = open("/home/textoenpython.txt", "w")
   file.write("GPIO.input("P9_23")" "round(soundVolt,3)" + os.linesep)
   file.write("Tengo hambre")
   file.close()
   x = np.linspace(GPIO.input("P9_23"),round(soundVolt,3))
   time.sleep(0.5)
   GPIO.output("P9_25",0)
   time.sleep(0.5)


plt.plot(x, x, label='linear')
plt.show()
