import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import decimal, time, cv2, sys
import matplotlib.pyplot as plt

#-----------FUNCIONES GLOBLES---------------------------
def coilOn(pin):   GPIO.output(pin, GPIO.HIGH);   return()
def coilOff(pin):  GPIO.output(pin, GPIO.LOW);    return()

#-------------DEFINIENDO FUNCIONES---------------
#Funcion de capturar foto
'''
def Foto(Nombre):
    video_capture=cv2.VideoCapture("/dev/video0") #Escogiendo la camara
    # Check success
    if not video_capture.isOpened(): raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()
    video_capture.release()    # Close device
    frameRGB = frame[:,:,::-1] # BGR => RGB
    #cv2.imshow(frameRGB, img)
    cv2.imwrite('/home/debian/'+str(Nombre),frameRGB)
    cv2.imshow('image',frameRGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
#Funcion de temperatura
def Temperatura(Pin):
    reading = ADC.read(Pin)
    milivolts = reading*1800
    temp_c = (milivolts / 10.0)+143.70-273.15
    return(float(temp_c))

#Funcion de Distancia
def Distancia(TRIG,ECHO):   #Define una funcion que depende del trigg$
    #Configuration
    GPIO.setup(TRIG,GPIO.OUT); GPIO.setup(ECHO,GPIO.IN) # Triger, Echo
    GPIO.output(TRIG, 1)  #Inicio del pulso
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:  pulseStart = time.time()
    while GPIO.input(ECHO) == 1:  pulseEnd = time.time()
    pulseDuration = pulseEnd - pulseStart   #dt
    distance = round(pulseDuration * 17150,1)        #dx=dt*vs/2

    return(distance)


#Funciones para mover el motor
def alloff():
 for i in range(4):
  #GPIO.setup("P8_%d",GPIO.OUT)
  GPIO.output("P8_%d" % (j*2+40), 0)
  return()
#Pines Para el motor
a="P8_40"
b="P8_42"
c="P8_44"
d="P8_46"
#Configurando pinde del motor
GPIO.setup("P8_40",GPIO.OUT)
GPIO.setup("P8_42",GPIO.OUT)
GPIO.setup("P8_44",GPIO.OUT)
GPIO.setup("P8_46",GPIO.OUT)

dt=1*10**-3
vueltas=1  #numero de vueltas
pasos=8 #numero de pasos por vuelta
hold=1 #espera entre pasos


def seQ1():
    coilOff(d);       coilOff(c);       coilOff(b);       coilOn(a)
    return()   #0001 =     a b c d
def seQ2():
    coilOff(d);       coilOff(c);       coilOn(b);       coilOff(a)
    return()   #0010
def seQ3():
    coilOff(a);       coilOff(b);       coilOn(c);       coilOff(d)
    return()   #0100
def seQ4():
    coilOn(d);       coilOff(c);       coilOff(b);       coilOff(a)
    return()   #1000

#Define Function for direction-Motor
def clockW():   #1-2-3- for anticlockwise direction
    seQ1()
    time.sleep(dt)
    seQ2()
    time.sleep(dt)
    seQ3()
    time.sleep(dt
    seQ4()
    time.sleep(dt)
    return()
def antiClockW():        #6-10-9-5 for clockwise direction
    seQ4()
    time.sleep(dt)
    seQ3()
    time.sleep(dt)
    seQ2() 
    time.sleep(dt)
    seQ1() 
    time.sleep(dt)
    return()

#Definiendo funcin de Audio
def Audio(pin):
    GPIO.setup(pin,GPIO.IN)
    return(GPIO.input(pin))

#----------------------------------------
#------------PROGRAMA PRINCIPAL------------
n=10.0   #numero de tomas
#vueltas=input(int("N  mero de vueltas: "))
#vueltas=1
tigger= "P9_25"; echo="P9_27";
pins="P9_13"
ADC.setup
pinT="P9_40"

for p in range((540)*vueltas):   #Por qu   ese n  mero por vueltas, 540?
      antiClockW()  #Gira el motor
      sound, distance,temperature = 0,0,0
      if p%(540/pasos)==0:    # para si esta en 1/pasoavo
       print('Tomando medidas: ')
       for j in range(10):
         print("Distancia: ",Distancia(tigger,echo)," cm" ,"   Sonido: ", Audio(pins)) #, "  Temperatura: ",Temperatura(pinT))
         #distance+=distancia(tigger,echo); sound+=sonido(pins)
         #print('Promedios:')
         #print("Distancia: ",round(distance/n,2)," cm","   Sonido: ", sound/n)
         #print('')
         time.sleep(hold)
#       time.sleep(hold)

#print(Sensores.Temperatura("P8_)) #Imprimer el valor de la temperatura
#print(Sensores.Distancia()) #Imprimer el valor de la temperatura
'''
n=10.0   #n  mero de tomas
for p in range((540)*vueltas):   #Por qu   ese n  mero por vueltas, 540?
      antiClockW()  #Gira el motor
      sound, distance = 0,0
      if p%(540/pasos)==0:    # para si esta en 1/pasoavo
       print('Tomando medidas: ')
       for j in range(10):
         print("Distancia: ",Distancia(tigger,echo)," cm","   Sonido: ", Audio(pin))
         distance+=Distancia(tigger,echo); sound+=Audio(pin)
       print('Promedios:')
       print("Distancia: ",round(distance/n,2)," cm","   Sonido: ", sound/n)
       print('')
       time.sleep(hold)
'''
