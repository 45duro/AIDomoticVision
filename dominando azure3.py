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
img_url = 'https://lh3.googleusercontent.com/7bhxO9aoPM0ilfaUwToYxNxsFBWDyl15Tb6x-wcFvOlxOSGE0AKCYVm5crCeb3I8vZVMkPU5TDAdKvznzzZsATwAeA8psEo0chchGYcUjXs9-SodTNZsVzfsLCt7afmz02--c0CNOqwd0Acm5owwhbf6P5ko0j5IlKFgxogyD-CxaPLve2pBMTZWyeNIHhQeD1a563dGf1P7qY5QYuCjFWIkXy1A-p-j4BlrVnk6_ryz2k3Wqqz1P3UED13HYjIJbxKv1TM2mghEXAzKjhtRdKSH_FMZhkbR6nlU2qOzAHnBJLlyfWQST7ESj5BqsOezKUkjecxTE5LfkteR88H5CGZTtIukVNqDodCHPEn_U1O7PBfFPjMuI2zLyWf8NIe6mfYY-2-xEqSez8dFxOfvdf5-FHTf7iQwtgLpVkM3bxUl7Tg_Ozo1V8nIgbsRcytueaxqUvACE_lLaw1iFAovVJHQ4qqYcPTEilGWNR9Kgj5SN4vBzQY4dFbCRtaE_i4xzBOaB0Utrn-2Ew3KPDmf_UKSBZYJjP3QONLGOxvNFuXD6BTePmDhF96OPukvaej8egmht-ZoRXJdSQLXDH2P-o8qajBbx0tIeZZq-yewzrZ12_X9HxnXc4cVid4zmgJ-FGAOT9pFqF4Y_mpJ2b4INSGFTJISAfVTntXxtk9PmpO-uAslp71PzCJd_OwtlmSabMBwdWtSOfmRjCDJJGLuGIQq=w876-h657-no'
faces = CF.face.detect(img_url)
print(faces)





#Añadir rectangulos a la imagen general
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    
    return ((left, top),(bottom, right))

def mostrarImagen(imagen):
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()


#Descargar la imagen de la url
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

#Para cada cara retornada use un rectangulo y dibuje una cara roja

draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')
 
 
#Muestre la imagen
img.show()

