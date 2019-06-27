import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import decimal, time
import Adafruit_BBIO.PWM as PWM
from KeypadSecuencias import *

#--------------------MOTOR-----------------

PinesMotor=["P8_32","P8_34","P8_36","P8_38"] #a,b,c,d

dt=1*10**-3
vueltas=1  #numero de vueltas
pasos=8 #numero de pasos por vuelta
hold=1 #espera entre pasos

#Haciendo todas las secuencias
SecuenciaSimple=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Secuencias=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
            [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]

for i in range(4): GPIO.setup(PinesMotor[i],GPIO.OUT)

def Pasos():
   for p in (range(64)):
    for secuencia in range(8):
        for pin in range(4):
          GPIO.output(PinesMotor[pin], Secuencias[7-secuencia][pin]) #Para el otro lado es quitar el 7-
        time.sleep(dt)

Pasos()
