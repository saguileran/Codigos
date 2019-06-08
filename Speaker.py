####Este es un tutorial del libro de Alexander Hiam pagina 45 del PDF####
import time
from Adafruit_BBIO import PWM
from Notas import *

led_pin = "P9_14" #Pin donde se coloca un PWM
PWM.start(led_pin, 0, 60)   #el segundo termino es the initial duty cycle, el tercero es la frecuencia
dt=0.1 #tiempo entre pulsos
#a=False  #Apagar ciclo
a=True  #Realiza el sonido

#Generando una onda
def wave(led_pin, frecuency, dt):   ##)pin, frecuency, duration/2)
 PWM.start(led_pin, 0, frecuency)   #el segundo termino es the initial duty cycle, el tercero es la frecuencia
 for level in range(0, 100):
   PWM.set_duty_cycle(led_pin, level)
   time.sleep(dt)
 for level in range(100, 0, -1): ##
   PWM.set_duty_cycle(led_pin, level)
   time.sleep(dt)
def nowave(pin):
 PWM.set_duty_cycle(led_pin, 0)
 return()
#Generando una nota definida
melody = [C4, G3, G3, A3, G3, 0, B3, C4]
noteDurations=[4,8,8,4,4,4,4,4]
  # iterate over the notes of the melody:

'''    #para comentar varias lineas
for thisNote in range(len(melody)):
 # to calculate the note duration, take one second divided by the note type.
 #e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
 noteDuration = int(1000 / noteDurations[thisNote])
 wave(led_pin, melody[thisNote], noteDuration)
  # to distinguish the notes, set a minimum time between them.
 # the note's duration + 30% seems to work well:
 pauseBetweenNotes = int(noteDuration * 1.3)
 time.sleep(pauseBetweenNotes)
 # stop the wave playing:
 nowave(led_pin)
'''

while(a):
  for level in range(0, 100):
   PWM.set_duty_cycle(led_pin, level)
   time.sleep(dt)
  for level in range(10, 0, -1):
   PWM.set_duty_cycle(led_pin, level)
   time.sleep(dt)
  a=0
#  a=int(input("Continuar 1, no continuar 0: ")) #Pide un valor al usuario
  if a==1:
    a=True
    b=float(input("Frecuencia nueva: "))
    PWM.start(led_pin, 0, b)   #el segundo termino es the initial duty cycle, el tercero es la frecuencia
  else: a=False
# except(KeyboardInterrupt):
PWM.cleanup()
