import cv2, sys, time
import matplotlib.pyplot as plt
import subprocess


def Foto(Nombre):

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
 a='/home/debian/'
 cv2.imwrite(a+Nombre ,frameRGB)
 cv2.imshow('image',frameRGB)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

print("Tomando Imagen")
Name="Camara.jpg"
Foto(Name)
print("FOto tomada")
bashCommand = "mv /home/debian/"+Name+" /home/debian/MicroSD/Codigos/Fotos"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()



