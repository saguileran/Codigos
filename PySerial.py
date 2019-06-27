'''
import serial
ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port
'''


# warning: untested code
import serial
serial_port = serial.Serial( port="/dev/ttyACM0", baudrate=9600, timeout=1 )
while True:
    serial_port.write("Hey.")
    print(serial_port.read())
