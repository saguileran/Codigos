import Adafruit_BBIO.GPIO as GPIO
import time

rows=4; cols=4;

#Definiendo la matrix
MATRIX = [ ['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D'] ]

#definiendo los pines
COL = ["P8_40","P8_42","P8_44","P8_46"] # C3, C3, C2, C1
ROW = ["P8_41","P8_43","P8_43","P8_45"] # R4, R3, R2, R1

#configura las salidas
for j in range (4):
    GPIO.setup(COL[j], GPIO.IN) #Colocando columnas como salidas
    GPIO.setup(ROW[j], GPIO.IN) #Colocando filas como entradas
#    GPIO.output(COL[j], 1)
while(True):
 for i in range(4):
  print("Columna, Fila")
  print(GPIO.input(COL[i]),GPIO.input(ROW[i])) #Columna, Fila
 print(' ')
 time.sleep(1)
#for i in range (4):
#    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

'''
#try:
while(True):
 for j in range (4):  GPIO.output(COL[j],0)
  for i in range (4):
   if GPIO.input (ROW[i]) == 0:
     print (MATRIX[i][j])
     while (GPIO.input(ROW[i]) == 0): pass

  GPIO.output(COL[j],1)
#except KeyboardInterrupt:
GPIO.cleanup()
'''
