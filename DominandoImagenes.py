import cv2
import numpy as np


def mostrarImagen(imagen):
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', imagen)
    cv2.waitKey()


filename = "LinuxLogo.jpg"

#Leer la imagen
img = cv2.imread(filename)

#leer en grises
#img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#Convertir a grises
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find minimum and maximum intensities
# Convertir  en negros y blancos sobelx
sobelx = cv2.Sobel(grey, cv2.CV_32F, 1, 0)
minVal = np.amin(sobelx)
maxVal = np.amax(sobelx)
draw = cv2.convertScaleAbs (sobelx, alpha = 255.0 / (maxVal - minVal), beta = -minVal * 255.0 / (maxVal - minVal))



#mi funcion para mostrar la imagen
mostrarImagen(draw)