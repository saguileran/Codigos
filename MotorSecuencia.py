import Adafruit_BBIO.GPIO as GPIO
import time

a="P8_40"
b="P8_42"
c="P8_44"
d="P8_46"

GPIO.setup("P8_40",GPIO.OUT)
GPIO.setup("P8_42",GPIO.OUT)
GPIO.setup("P8_44",GPIO.OUT)
GPIO.setup("P8_46",GPIO.OUT)

dt=1*10**-3
vueltas=1  #numero de vueltas
pasos=8 #numero de pasos por vuelta
hold=5 #espera entre pasos

#Define function for making coil on and off 
def coilOn(pin):
      #GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.HIGH)
      return

def coilOff(pin):
      #GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
      return

def alloff():
 for i in range(4):
  j=i*2+40
  GPIO.output("P8_%d" % j, 0)
 return

#0001 =     a b c d
def seQ1():
       coilOff(d);       coilOff(c);       coilOff(b);       coilOn(a)
       return
#0010
def seQ2():
       coilOff(d);       coilOff(c);       coilOn(b);       coilOff(a)
       return
#0100
def seQ3():
       coilOff(a);       coilOff(b);       coilOn(c);       coilOff(d)
       return
#1000
def seQ4():
       coilOn(d);       coilOff(c);       coilOff(b);       coilOff(a)
       return

#Define Function for direction
#1-2-3- for anticlockwise direction
def clockW():
       seQ1()
       time.sleep(dt)
       seQ2()
       time.sleep(dt)
       seQ3()
       time.sleep(dt)
       seQ4()
       time.sleep(dt)
       return

#6-10-9-5 for clockwise direction
def antiClockW():
       seQ4()
       time.sleep(dt)
       seQ3()
       time.sleep(dt)
       seQ2()
       time.sleep(dt)
       seQ1()
       time.sleep(dt)
       return

#define Main program
print("Python Programa for Stepper Motor")
print(" ")

for p in range((520)*vueltas):
  antiClockW()
  if p%(540/pasos)==0: time.sleep(hold)

for p in range((560)*vueltas):
  clockW()
  if p%(540/pasos)==0: time.sleep(hold)

for p in range((520)*vueltas):
  antiClockW()
  if p%(540/pasos)==0: time.sleep(hold)

for p in range((560)*vueltas):
  clockW()
  if p%(540/pasos)==0: time.sleep(hold)



