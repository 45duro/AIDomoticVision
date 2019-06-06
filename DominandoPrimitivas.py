##DIBUJAR PRIMITIVAS

import numpy as np
import cv2

def mostrarImagen(imagen):
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    
    #Creacion del array
    #recuerda (profundo, alto, ancho) ;D
    img = np.zeros((512, 512, 3), np.uint8)
    
    ##line((punto-inicio), (puinto fin), (colores BGR), ancho_pixeles)
    img = cv2.line(img,(0,0),(511,511),(100,180,255),100)
    
    ##Rectangle(img,(punto_inicio),(puinto_fin),(colores BGR),ancho_pixeles)
    img = cv2.rectangle(img,(100,0),(510,128),(0,255,0),20)
    
    ##ellipse(img,(centro) ,(Ancho, Alto),giro,lapiz,cubrido,(b,g,r),ancho_contorno)
    img = cv2.ellipse(img,(255,255) ,(100,200),0,0,360,(0,255,0),-1)
    
    #Puntos de la polilinea
    pts = np.array([[0,0],[100,200],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    
    img = cv2.polylines(img,[pts],True,(255,255,255))
    
    #Colocar Texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #putText(VariableDondeColocar,'Tecnobot',(origenX,Y), (fuente), (linea),(B,G,R),(ancho_contorno),cv2.LINE_AA)
    cv2.putText(img,'Tecnobot',(10,500), font, 1.5,(0,255,0),2,cv2.LINE_AA)
    print(pts)
                
    mostrarImagen(img)
    return

if __name__ == '__main__':
    main()