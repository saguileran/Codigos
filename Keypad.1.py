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
ROW = ["P8_45","P8_37","P8_35","P8_39"] # R1, R2, R3, R4

for h in range(4):
 GPIO.setup(COL[h],GPIO.OUT)
 GPIO.setup(ROW[h],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def TurnOff(COL):
 for q in range(4): GPIO.output(COL[q],0)

#Intento
for w in range(4): print("Fila (In): ",GPIO.input(ROW[w]),"COl :",GPIO.input(COL[w]))
print(" ")
#for p in range(4): print(GPIO.input(ROW[p]),GPIO.input(COL[p]))
flat=0,0
for i in range(1000):
  for j in range(4): #j es la columna
   GPIO.output(COL[j],1)
   for k in range(4):
     if GPIO.input(ROW[k])==1: flat=j,k
   TurnOff(COL)
  for p in range(4): print(GPIO.input(ROW[p]),GPIO.input(COL[p]))
  print(" ")
  time.sleep(0.1)
  print(MATRIX[flat[1]][flat[0]])

