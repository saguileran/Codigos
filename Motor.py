import Adafruit_BBIO.GPIO as GPIO
import time

Pines=["P8_8","P8_10","P8_12","P8_14"]
for i in range(4):
 GPIO.setup(Pines[i],GPIO.OUT)
def turoff(pines):
 for i in range(4):  GPIO.output(pines[i],0)
 return()

wait=0.007
nVueltas=3

for i in range(540*nVueltas):
 for j in range(4):
  turoff(Pines)
  if (8+j*2)==8: GPIO.output("P8_8",GPIO.HIGH)
  if (8+j*2)==10: GPIO.output("P8_10",GPIO.HIGH)
  if (8+j*2)==12: GPIO.output("P8_12",GPIO.HIGH)
  if (8+j*2)==14: GPIO.output("P8_14",GPIO.HIGH)
  time.sleep(wait)



