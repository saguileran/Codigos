import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()
A=True
pin="P9_40"
#=False

while(A):
 reading = ADC.read(pin)
 milivolts = reading*1800
 temp_c = milivolts / 10
 print(temp_c)
 time.sleep(1)
