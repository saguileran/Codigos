import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time, math
from decimal import *
#GPIO.setup()
#GPIO.setup("P9_11", GPIO.OUT )
a="P9_13"
GPIO.setup(a, GPIO.IN)
#GPIO.setup("")

#value=GPIO.input(a,GPIO.IN)
for i in range(10000):
 print(GPIO.input("P9_13"))
   


 # print(value*1.8)
  
#GPIO.output("P9_11",0)

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
for i in range(2000):
   soundVal=ADC.read(analogPin)*1.8 #*3.42*1000
   decibel=20*math.log10(soundVal/1.8)
   #s.append(soundVal)   #Creando una lsita
  # soundVolt=soundVal*1000 #*1.7*1000
  # print "The Voltage is: "+str(soundVal)+" V"
   #print "The decibel is: "+str(decibel)+" dB"
#print(round(ADC.read(analogPin),10),str(round(soundVal,2))+" ", str(decibel)+str(" dB"))
#   print(round(soundVolt,3))
   #time.sleep(0.5)
   #GPIO.output("P9_25",0)
   suma+=soundVal
   suma0+=decibel
   time.sleep(1)
print("Promedio")
print(str(suma/20),str(round(suma0/20,2))+" dB")
