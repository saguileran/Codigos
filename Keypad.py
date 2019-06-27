import Adafruit_BBIO.GPIO as GPIO
import time

rows=4; cols=4;

#Definiendo la matrix
MATRIX = [ ['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D'] ]

#definiendo los pines
#COL = ["GPIO_66", "GPIO_69","GPIO_45","GPIO_47"] # C1, C2, C3, C4
#ROW = ["GPIO_67","GPIO_68","GPIO_44","GPIO_26"] # R1, R2, R3, R4
COL = ["P8_46","P8_44","P8_42","P8_40"] # C1, C2, C3, C4
ROW = ["P8_45","P8_43","P8_41","P8_39"] # R1, R2, R3, R4

for h in range(4):
 GPIO.setup(COL[h],GPIO.out)
 GPIO.setup(ROW[h],GPIO.input)

def TurnOF(COL):
   GPIO.output(COL[j],0)

#Intento1

flat=0,0
for i in range(200):
  for j in range(4):
   GPIO.output(COL[j])
   for k in range(4):
     if GPIO.input(ROW[k])==1:
      flat=j,k
   TurnOff(COL)
print(MATRIX[flat[0]][flat[1]])


#   GPIO.output(COL[j], 0) #Colocando columnas como salidas
#configura las salidas
'''
for j in range (4):
    GPIO.setup(COL[j], GPIO.OUT) #Colocando columnas como salidas
    TurnOff(COL)
    GPIO.setup(ROW[j], GPIO.IN) #Colocando filas como entradas
   #GPIO.output(COL[j], 1)
while(True):
 for i in range(100):
  flat,row=0,[]
  for j in range(4):
    GPIO.output(COL[j])
    for k in range(4):
     if GPIO.input(ROW[k])==1: flat=k
  if flat!=
 time.sleep(0.001)

'''
print("Columna, Fila")
 for i in range(4):
  #print("Columna, Fila")
  #print(" ",GPIO.input(COL[i]),GPIO.input(ROW[i])) #Columna, Fila
  #print()
  print("C"+str(i+1),GPIO.input(COL[i]),"F"+str(i+1),GPIO.input(ROW[i])) #Columna, Fila
 print(' ')
 time.sleep(0.1)
#for i in range (4):
#    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

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
