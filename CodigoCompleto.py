import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import decimal, time, cv2, sys
import matplotlib.pyplot as plt

#-----------FUNCIONES GLOBLES---------------------------
def coilOn(pin):   GPIO.output(pin, GPIO.HIGH);   return()
def coilOff(pin):  GPIO.output(pin, GPIO.LOW);    return()

#-------------DEFINIENDO FUNCIONES---------------
#Funcion de capturar foto
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

#Funcion de temperatura
def Temperatura(Pin):
    ADC.setup
    reading = ADC.read(Pin)
    milivolts = reading*1800
    temp_c = milivolts / 10.0
    return(temp_c)

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
def alloff(pines):
    for i in range(len(pines)):
        GPIO.setup(pines[i], GPI.OUT)
        GPIO.output(pines[i], 0)   
        return()
dt=0.1
pasos=8
#Pines Para el motor
a="P8_8"
b="P8_10"
c="P8_12"
d="P8_14"
#Configurando pinde del motor
GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)

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
def antiClockW():   #1-2-3- for anticlockwise direction
    seQ1(); time.sleep(dt);      seQ2(); time.sleep(dt);
    seQ3(); time.sleep(dt);      seQ4(); time.sleep(dt);
    return()
def clockW():        #6-10-9-5 for clockwise direction
    seQ4(); time.sleep(dt);       seQ3(); time.sleep(dt);
    seQ2(); time.sleep(dt);       seQ1(); time.sleep(dt);
    return()

#Definiendo funcin de Audio
def Audio(pin):
    GPIO.setup(pin,GPIO,IN)
    return(GPIO,input(pin))

#----------------------------------------
#------------PROGRAMA PRINCIPAL------------
n=10.0   #numero de tomas
#vueltas=input(int("Número de vueltas: "))
vueltas=1
tigger= "P9_25"; echo="P9_27";

for p in range((540)*vueltas):   #Por qué ese número por vueltas, 540?
      antiClockW()  #Gira el motor
      sound, distance,temperature = 0,0,0
      if p%(540/pasos)==0:    # para si esta en 1/pasoavo
       print('Tomando medidas: ')
       for j in range(10):
         print("Distancia: ",Distancia(tigger,echo)," cm") #,"   Sonido: ", sonido(pin),)
         #distance+=distancia(tigger,echo); sound+=sonido(pin)
       #print('Promedios:')
       #print("Distancia: ",round(distance/n,2)," cm","   Sonido: ", sound/n)
       #print('')
         time.sleep(0.1)


#print(Sensores.Temperatura("P8_)) #Imprimer el valor de la temperatura
#print(Sensores.Distancia()) #Imprimer el valor de la temperatura
