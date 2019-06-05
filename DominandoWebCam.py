import numpy as np
import cv2

def main():
    #camaraWeb()
    #cargarVideo()
    guardarVideo()
    return

def camaraWeb():
    cap = cv2.VideoCapture(0)
    
    while(True):
        #Capture frame * Frame
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
    #Cuando todo esté hecho, terminar la captura
    cap.release()
    cv2.destroyAllWindows()

def cargarVideo():
    cap=cv2.VideoCapture("video1.mp4")
    
    while (cap.isOpened()):
        ret, frame = cap.read()
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Si quiere usar el gre lo coloca sino noj
        cv2.imshow("frame", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    

def guardarVideo():
    cap = cv2.VideoCapture(0)
    
    #Definimos el coder a usar
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    #Escribirlo en OUT
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret==True:
            out.write(frame)
            cv2.imshow('joder', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        
        
    #Cerrar la conexion
    cap.release()
    out.release()
    cv2.destroyAllWindows()
        


if __name__ == '__main__':
    main()