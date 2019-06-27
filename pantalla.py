import serial
s=serial.Serial("/dev/ttyACM0",baudrate=9600)
s.write(b"wjhgchgchgsdnwjd\r")
