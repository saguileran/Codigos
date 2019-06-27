import cv2
import sys
import matplotlib.pyplot as plt

#video_capture = cv2.VideoCapture(0)
video_capture=cv2.VideoCapture("/dev/video0") #Escogiendo la camara
# Check success
if not video_capture.isOpened():
   raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()
# Close device
video_capture.release()
#print(ret)
#img = cv2.imread('1.jpg',1)  #Leyendo imagenes
#print(frame.shape)
frameRGB = frame[:,:,::-1] # BGR => RGB
#cv2.imshow(frameRGB, img)
#cv2.imwrite('/home/debian/MicroSD/Codigos/Fotos/CameraPhoto.jpg',frameRGB)
cv2.imwrite('/home/debian/Fotos/CameraPhoto.jpg',frameRGB)
cv2.imshow('image',frameRGB)
cv2.waitKey(0)
cv2.destroyAllWindows()

