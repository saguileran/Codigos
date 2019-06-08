import time
  
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
  
import Image
import ImageDraw
import ImageFont

#Beaglebone Black hardware SPI config:
DC = 'P9_15'
RST = 'P9_12'
SPI_PORT = 1
SPI_DEVICE = 0
disp = LCD.PCD

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)
 
# Clear display.
disp.clear()
disp.display()

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
 
# Draw some shapes.
draw.ellipse((2,2,22,22), outline=0, fill=255)
draw.rectangle((24,2,44,22), outline=0, fill=255)
draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
draw.line((68,22,81,2), fill=0)
draw.line((68,2,81,22), fill=0)
 
# Load default font.
font = ImageFont.load_default()
 
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
 
# Write some text.
draw.text((8,30), 'Hello World!', font=font)
 
# Display image.
disp.image(image)
disp.display()
