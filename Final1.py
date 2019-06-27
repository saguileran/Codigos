import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import decimal, time, serial
import Adafruit_BBIO.PWM as PWM
from KeypadSecuencias import *
from TomandoImagen1 import *

Arduino =serial.Serial("/dev/ttyACM0", 9600)
#-------------FUNCIONES GLOBAES--------
ADC.setup()

#--------------------MOTOR-----------------

#SecuenciaSimple=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def Paso(PinesMotor,Paradas,Direccion): #1 derecha, -1 izquieda
    Secuencias=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
                [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]] #Secuencia que sigue
    pasos=int(512/Paradas)

    for i in range(4): GPIO.setup(PinesMotor[i],GPIO.OUT)

    for p in (range(pasos)):
        for secuencia in range(8):
            for pin in range(4):
                if Direccion==1: j=7-secuencia
                else:  j=secuencia
                GPIO.output(PinesMotor[pin], Secuencias[j][pin])
            time.sleep(0.001)
#-----------------SONIDO----------------------------

def Sonido(pin):  return(GPIO.input(pin))

#------------------TEMPERATURA-----------------------

def Temperatura(PinTemperatura):
    reading = ADC.read(PinTemperatura)
    milivolts = reading*1800
    temp_c =(milivolts / 10.0)+143.70-273.15
    return(round(temp_c,0))

#---------------DISTANCIA--------------------------

def Distancia(TRIG,ECHO):   #Define una funcion que depende del trigger

    GPIO.output(TRIG, True)  #Inicio del pulso
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:    pulseStart = time.time()
    while GPIO.input(ECHO) == 1:    pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart   #dt
    distance = pulseDuration * 17150        #dx=dt*vs/2

    return(round(distance,1))

#------------------TECLADO------------------------
COLS = ["P8_46","P8_44","P8_42","P8_40"] # C4, C3, C2, C1
ROWS = ["P8_45","P8_43","P8_41","P8_39"] # R4, R3, R2, R1

def Preguntando():
# if Teclado(COLS,ROWS)[1]==0: return(int(Teclado(COLS,ROWS)[0]))
# else:
 con=True
 while con==True:
  print("Numero: ")
  a=Teclado(ROWS,COLS)
  if type(a)!=None: return(a); con=False
  else: pass


def DosDigitos():
 print("?")
 a= Teclado(ROWS,COLS)[0]
 if a!='None':
  print(a)
 # time.sleep(0.5)
  b= Teclado(ROWS,COLS)[0]
  if b!='None':
    print(b)
    c=a+b
 return(int(c))

#---------------------CODIGO PRINCIPAL----------------
#Definiendo constantes
PinesMotor=["P8_32","P8_34","P8_36","P8_38"] #a,b,c,d
pasos=Preguntando()
#pasos=2 #numero de pasos por vuelta
Espera=1 #Espera entre cada paso

PinAudio="P8_28";  GPIO.setup(PinAudio, GPIO.IN)

PinTemperatura="P9_40"

Tigger= "P9_25";   GPIO.setup(Tigger,GPIO.OUT) #Trigger
Echo="P9_27";      GPIO.setup(Echo,GPIO.IN) #ECHO

COLS = ["P8_46","P8_44","P8_42","P8_40"] # C4, C3, C2, C1
ROWS = ["P8_45","P8_43","P8_41","P8_39"] # R4, R3, R2, R1
N=10 #numero de tomas

Angulos=list(range(0,361,int(360/pasos)))
MedicionesPorAngulo=[]
Medicion=len(Angulos)


#print(DosDigitos())


for l in range(pasos+1):
 Promedios=[0,0,0]  #distancia, sonido, temperatura
 for j in range(N): #Toma de las N mediciones
   Mediciones=[round(Distancia(Tigger,Echo),1), round(Sonido(PinAudio),1), round(Temperatura(PinTemperatura),2)]
   #print("Distancia: ",Distancia(Tigger,Echo)," cm","   Sonido: ", Sonido(PinAudio), "   Temperatura: ",Temperatura(PinTemperatura), " C")
   for p in range(3): Promedios[p]+=round(Mediciones[p]/N,2)
   time.sleep(1/N)
 print(Promedios)
 text="{} {} {}"-format(Promedios[0],Promedios[1],Promedios[2])
 Arduino.write(text.encode())
 MedicionesPorAngulo.append(Promedios)
 Foto("Foto"+str(l)+".jpg")
 time.sleep(Espera)
 if l!=pasos:Paso(PinesMotor,pasos,1) #1 derecha, -1 izquieda

#for k in range(pasos):
# print(Angulos[k],MedicionesPorAngulo[k])
#print(Angulos,len(MedicionesPorAngulo))
