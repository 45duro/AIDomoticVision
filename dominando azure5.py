

import requests
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF
import cv2

KEY = 'b0655492a6224e5f8b272d92cbd1138c'
CF.Key.set(KEY)


#Extremo de Conexion
BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

#Imagen a analizar
#img_url = 'https://lh3.googleusercontent.com/7bhxO9aoPM0ilfaUwToYxNxsFBWDyl15Tb6x-wcFvOlxOSGE0AKCYVm5crCeb3I8vZVMkPU5TDAdKvznzzZsATwAeA8psEo0chchGYcUjXs9-SodTNZsVzfsLCt7afmz02--c0CNOqwd0Acm5owwhbf6P5ko0j5IlKFgxogyD-CxaPLve2pBMTZWyeNIHhQeD1a563dGf1P7qY5QYuCjFWIkXy1A-p-j4BlrVnk6_ryz2k3Wqqz1P3UED13HYjIJbxKv1TM2mghEXAzKjhtRdKSH_FMZhkbR6nlU2qOzAHnBJLlyfWQST7ESj5BqsOezKUkjecxTE5LfkteR88H5CGZTtIukVNqDodCHPEn_U1O7PBfFPjMuI2zLyWf8NIe6mfYY-2-xEqSez8dFxOfvdf5-FHTf7iQwtgLpVkM3bxUl7Tg_Ozo1V8nIgbsRcytueaxqUvACE_lLaw1iFAovVJHQ4qqYcPTEilGWNR9Kgj5SN4vBzQY4dFbCRtaE_i4xzBOaB0Utrn-2Ew3KPDmf_UKSBZYJjP3QONLGOxvNFuXD6BTePmDhF96OPukvaej8egmht-ZoRXJdSQLXDH2P-o8qajBbx0tIeZZq-yewzrZ12_X9HxnXc4cVid4zmgJ-FGAOT9pFqF4Y_mpJ2b4INSGFTJISAfVTntXxtk9PmpO-uAslp71PzCJd_OwtlmSabMBwdWtSOfmRjCDJJGLuGIQq=w876-h657-no'
img_url = "https://lh3.googleusercontent.com/NMjZ7vj3uUkoDRolXm_WUPJsIauxxAtdmBTjqavZD6bTSkrcqI_0b3GY1JiloA6zEvtxFIJ7MLPodmMnuhKsKr4s7gFKIHk5hfuZ1MlSrlsfYDyxLa7F8-yhTfBC3e_x11t3kz1qRU9XbrXhNHVIPMpoN7JBhd2HC5dvX_Y19VfC0B9sP5hDiKjC1F6mkXNgBPd2E0K9tmP3DAPq5cME3Tq0-ZtpL-gvUIk3zIgDNplZRvBma8Djbf4je6Nou88sOQP2Noc0tgs3is18ivC-n89Mp47lhonrcEapKLuNatcKEmWA13aDESTzL4N5dFj7nHC3tOE2K1XlmZPOl2soEa7cKM3cqwQWEiyEgeZ-PETdePCNbMr5xvqsDllSFlH2-xg1mlTlwVrUyDprLhHFHAIhZHj_cIkaQECYebhzjB8aVppP8Tuo7VHhiMMEY6fPwHcLSIgzyneifIfTFB8aKYV5i3wdEHDhYwma237QvN8qMlI3XtV3oGHofbd0-vGtpQSmpaR0OObS7nkF2bX2UP8t1HsbDrKoHLK_oSugV1oCzU53waTGU-K6yhmUp-WHXvmDRuGHs9mWYTAHmv4X21ldMwjGjnGJhcsxNqSyOX7hEN3KhC4Lo7501ldJXnAD-JDA2jktKuzrgpqh0HjzMDIJ_muBSRhd_VAngPs82HVTZbwZttiHo_FX_umtmaiBmOuU9Cmago3f9v-WvJFrAe95=w843-h632-no"
#faces = CF.face.detect(img_url)

faces= CF.face.detect(img_url, face_id=True, landmarks=True, attributes='age')


#print(faces)





#Añadir rectangulos a la imagen general
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    
    return ((left, top),(bottom, right))

#Añadir puntos de reconocimiento a la imagen general
def getPartes(faceDictionary):
    part = faceDictionary['faceLandmarks']
    ojos = part['eyeLeftOuter']
    mouthLeft = part['mouthLeft']
    underLipBottom = part['underLipBottom']
    noseRootRight = part['noseRootRight']
    
    return ((ojos['x'],ojos['y']), (mouthLeft['x'],mouthLeft['y']),(underLipBottom['x'],underLipBottom['y']),(noseRootRight['x'],noseRootRight['y']))

#Extraer la edad en texto
def getEdad(faceDictionary):
    atributos = faceDictionary['faceAttributes']
    edad = atributos['age']
    
    return ("Edad: " + str(edad))


#Descargar la imagen de la url
response = requests.get(img_url)
print(response)
img = Image.open(BytesIO(response.content))

#Para cada cara retornada use un rectangulo y dibuje una cara roja

draw = ImageDraw.Draw(img)
for face in faces:
    
    #Extraer punto de inicio del texto
    PuntoCuadro = getRectangle(face)
    texto_X = PuntoCuadro[0][0]
    texto_Y = PuntoCuadro[0][1] - 10
    draw.text((texto_X, texto_Y), getEdad(face), fill=None, font=None, anchor=None)
    
    draw.rectangle(getRectangle(face), outline='red')
    draw.point(getPartes(face), fill='green')
    
 
#Muestre la imagen
img.show()

