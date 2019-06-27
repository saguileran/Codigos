#para conectar LM335:

# Resistencia de 2k
# 2 Resistencias de 10k
# 5 voltios de alimentacion: P9_8

import Adafruit_BBIO.ADC as ADC
import time

sensor_pin = 'P9_36'
N=100
ADC.setup()
reading = ADC.read(sensor_pin)
read = reading * 1800
temp = (read) / 10
#print(reading,read,temp)
promedio=0

for i in range (0,20000):
  reading = ADC.read(sensor_pin)
  millivolts = reading * 1800   # 1.8V reference = 1800 mV #intentar poniendo 1100mV
  temp_k = (millivolts / 10)+ 141  #10mV = 1 K 
  temp_c= temp_k - 273.15
  #print (reading)
  print('mv=%d K=%d ''C=%d' % (millivolts, temp_k, temp_c))
  promedio+=temp_c
  time.sleep(1)
print(round(promedio/200,2))
