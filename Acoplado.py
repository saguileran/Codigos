import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import decimal, time
from KeypadSecuencias import *

a="P8_32"
b="P8_34"
c="P8_36"
d="P8_38"

GPIO.setup("P8_32",GPIO.OUT)
GPIO.setup("P8_34",GPIO.OUT)
GPIO.setup("P8_36",GPIO.OUT)
GPIO.setup("P8_38",GPIO.OUT)

dt=1*10**-3
vueltas=1  #numero de vueltas
pasos=8 #numero de pasos por vuelta
hold=1 #espera entre pasos

#Define function for making coil on and off
def coilOn(pin):
   GPIO.output(pin, GPIO.HIGH)
   return()

def coilOff(pin):
  GPIO.output(pin, GPIO.LOW)
  return()

def alloff():
 for i in range(8,15,2):
  #GPIO.setup("P8_%d",GPIO.OUT)
  GPIO.output("P8_%d" % j, 0)
  return()

#0001 =     a b c d
def seQ1():
       coilOff(d);       coilOff(c);       coilOff(b);       coilOn(a)
       return()
#0010
def seQ2():
       coilOff(d);       coilOff(c);       coilOn(b);       coilOff(a)
       return()
#0100
def seQ3():
       coilOff(a);       coilOff(b);       coilOn(c);       coilOff(d)
       return()
#1000
def seQ4():
       coilOn(d);       coilOff(c);       coilOff(b);       coilOff(a)
       return()

#Define Function for direction
#1-2-3- for anticlockwise direction
def clockW():
       seQ1(); time.sleep(dt)
       seQ2(); time.sleep(dt)
       seQ3(); time.sleep(dt)
       seQ4(); time.sleep(dt)
       return()

#6-10-9-5 for clockwise direction
def antiClockW():
       seQ4(); time.sleep(dt)
       seQ3(); time.sleep(dt)
       seQ2(); time.sleep(dt)
       seQ1(); time.sleep(dt)
       return()

#_________________________________________________________________________
def distanceMeasurement(TRIG,ECHO):   #Define una funcion que depende del trigg$

    GPIO.output(TRIG, True)  #Inicio del pulso
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart   #dt
    distance = pulseDuration * 17150        #dx=dt*vs/2
    distance = round(distance, 2)           #Redondea el valor de la distancia $

    return(distance)
    pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
     pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart   #dt
    distance = pulseDuration * 17150        #dx=dt*vs/2
    distance = round(distance, 2)           #Redondea el valor de la distancia $
    return(distance)

#######Definiendo funcion de medicion de audio#############33
pin="P9_13"
GPIO.setup(pin, GPIO.IN)
ADC.setup()
suma=0
def sonido(pin): return(GPIO.input(pin))


##Configurando pines para medir distancia
tigger= "P9_25"; echo="P9_27";
GPIO.setup(tigger,GPIO.OUT) #Trigger
GPIO.setup(echo,GPIO.IN) #ECHO
def distancia(tigger,echo):  return(distanceMeasurement(tigger,echo))

###Funcion para medir temperatura
pin1="P9_40"
def temperatura(pin1):
 #ADC.setup
 reading = ADC.read(pin1)
 milivolts = reading*1800
 temp_c =(milivolts / 10.0)+143.70-273.15
 return(float(temp_c))


#############################Main code######
####TECLADO###
'''
COLS = ["P8_46","P8_44","P8_42","P8_40"] # C4, C3, C2, C1
ROWS = ["P8_45","P8_43","P8_41","P8_39"] # R4, R3, R2, R1
print("Si desea tomar medidas presione * ")
if(Teclado(COLS,ROWS)=='*'):
 n=10.0   #n  mero de tomas
 for p in range((540)*vueltas):   #Por qu   ese n  mero por vueltas, 540?
      clockW()  #Gira el motor
      sound, distance, temperature = 0,0,0
      if p%(540/pasos)==0:    # para si esta en 1/pasoavo
       print('Tomando medidas: ')
       for j in range(10):
         print("Distancia: ",distancia(tigger,echo)," cm","   Sonido: ", sonido(pin),
               "   Temperatura: ",round(temperatura(pin1),0), "C")
         distance+=distancia(tigger,echo); sound+=sonido(pin); temperature+=temperatura(pin1)
       print('PROMEDIOS:')
       print("Distancia: ",round(distance/n,2)," cm","   Sonido: ", sound/n,
        " Temp: ", round(temperature/n,0), " C")
       print('')
       time.sleep(hold)
'''
for p in range((540)*vueltas):   #Por qu   ese n  mero por vueltas, 540?
      antiClockW()  #Gira el motor
      sound, distance, temperature = 0,0,0
      if p%(540/pasos)==0:    # para si esta en 1/pasoavo
       print('Tomando medidas: ')
       for j in range(10):
         print("Distancia: ",distancia(tigger,echo)," cm","   Sonido: ", sonido(pin),
              "   Temperatura: ",round(temperatura(pin1),2), "C")
         distance+=distancia(tigger,echo); sound+=sonido(pin); temperature+=temperatura(pin1)
       print('PROMEDIOS:')
       print("Distancia: ",round(distance/n,2)," cm","   Sonido: ", sound/n,
        " Temp: ", round(temperature/n,0), " C")
       print('')
       time.sleep(hold)

else: print('Numero equivocado')


