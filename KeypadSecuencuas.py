import Adafruit_BBIO.GPIO as GPIO

ROWS = [10,11,12,13]
COLS = [6,7,8,9]

GPIO.output(COLS[0],HIGH);
GPIO.output(COLS[1],LOW);
GPIO.output(COLS[2],LOW);
GPIO.output(COLS[3],LOW);

if    (GPIO.input(ROWS[0] == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):    print("1");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   print("4");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):   print("7");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):   print("*");
else: timpe.sleep(100);

GPIO.output(COLS[0],LOW);
GPIO.output(COLS[1],HIGH);
GPIO.output(COLS[2],LOW);
GPIO.output(COLS[3],LOW);

if:   (GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):    print("2");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):    print("5");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):    print("8");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):    print("0");
else: time.sleep(100);

GPIO.output(COLS[0],LOW);
GPIO.output(COLS[1],LOW);
GPIO.output(COLS[2],HIGH);
GPIO.output(COLS[3],LOW);

if(GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):        print("3");
elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):      print("6");
elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):      print("9");
elif(GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):      print("#");
else:  time.sleep(100);

GPIO.output(COLS[0],LOW);
GPIO.output(COLS[1],LOW);
GPIO.output(COLS[2],LOW);
GPIO.output(COLS[3],HIGH);

if:   (GPIO.input(ROWS[0]) == HIGH and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   print("A");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == HIGH and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == LOW):   print("B");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == HIGH and GPIO.input(ROWS[3]) == LOW):   print("C");
elif: (GPIO.input(ROWS[0]) == LOW and GPIO.input(ROWS[1]) == LOW and GPIO.input(ROWS[2]) == LOW and GPIO.input(ROWS[3]) == HIGH):   print("D");
else: time.sleep(100);
