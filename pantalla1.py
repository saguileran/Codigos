import serial, time
arduino = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)
text=input("Escribir :")
arduino.write(text.encode())
arduino.close()
