import Adafruit_BBIO.GPIO as GPIO
import time

#Definiendo la matrix
MATRIX = [ ['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D'] ]

#definiendo los pines
#COL = ["GPIO_66", "GPIO_69","GPIO_45","GPIO_47"] # C1, C2, C3, C4
#ROW = ["GPIO_67","GPIO_68","GPIO_44","GPIO_26"] # R1, R2, R3, R4
COLS = ["P8_46","P8_44","P8_42","P8_40"] # C1, C2, C3, C4
ROWS = ["P8_45","P8_43","P8_41","P8_39"] # R1, R2, R3, R4

HIGH=1; LOW=0

def Teclado(COLS,ROWS):

 for i in range(4):
  GPIO.setup(COLS[i],GPIO.OUT)
  GPIO.setup(ROWS[i],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

 for i in range(100):
  GPIO.output(COLS[0],HIGH);
  GPIO.output(COLS[1],LOW);
  GPIO.output(COLS[2],LOW);
  GPIO.output(COLS[3],LOW);

  if    (GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   return(int(1)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   return(int(2)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):   return(int(3)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH): d=1;  return(str("A")); break;
  else: time.sleep(0.001);

  GPIO.output(COLS[0],LOW);
  GPIO.output(COLS[1],HIGH);
  GPIO.output(COLS[2],LOW);
  GPIO.output(COLS[3],LOW);

  if   (GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):    return(int(4)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):    return(int(5)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):    return(int(6)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):    return(str("B")); break;
  else: time.sleep(0.001);

  GPIO.output(COLS[0],LOW);
  GPIO.output(COLS[1],LOW);
  GPIO.output(COLS[2],HIGH);
  GPIO.output(COLS[3],LOW);

  if(GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):        return(int(7)); break;
  elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):      return(int(8)); break;
  elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):      return(int(9)); break;
  elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):    return(str("C")); break;
  else:  time.sleep(0.001);

  GPIO.output(COLS[0],LOW);
  GPIO.output(COLS[1],LOW);
  GPIO.output(COLS[2],LOW);
  GPIO.output(COLS[3],HIGH);

  if   (GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   return(str("*")); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   return(int(0)); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):   return(str("#")); break;
  elif (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):   return(str("D")); break;
  else: time.sleep(0.001);


#while True:
# print(type(Teclado(COLS,ROWS)), print(Teclado(ROWS,COLS)))
# time.sleep(0.001)
