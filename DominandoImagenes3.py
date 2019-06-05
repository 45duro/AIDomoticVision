import cv2
import numpy as np
from matplotlib import pyplot as plt

#filename = "LinuxLogo.jpg"
filename = "WindowsLogo.jpg"

def mostrarImagen(imagen):
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    #Cargar imagen
    img=cv2.imread(filename)
    
    #cargar imagen en grises
    #img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    #Guardar imagen
    #cv2,imwrite('otraImagen.jpg', img)
    
    #Mostrar imagen
    mostrarImagen(img)
    
    matploit(img)
    return

def matploit(imagen2):
    
    #Recibe solamente un archivo
    imagen = cv2.imread(filename)
    plt.imshow(imagen)
    plt.xticks([]), plt.yticks([])
    plt.show()
    return


main()
