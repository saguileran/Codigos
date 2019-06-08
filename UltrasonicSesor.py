import Adafruit_BBIO.GPIO as GPIO
import time

def distanceMeasurement(TRIG,ECHO):   #Define una funcion que depende del trigger y del echo

    GPIO.output(TRIG, True)  #Inicio del pulso
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart   #dt
    distance = pulseDuration * 17150        #dx=dt*vs/2
    distance = round(distance, 2)           #Redondea el valor de la distancia a 2 cifras
    return distance

#Configuration
GPIO.setup("P9_27",GPIO.OUT) #Trigger
GPIO.setup("P9_29",GPIO.IN)  #Echo

for i in range(0,200):
               recoveredDistance = distanceMeasurement("P9_27","P9_29")    #Calcula la distancia 
               print "Distance1: ",recoveredDistance,"cm"
               time.sleep(1)
