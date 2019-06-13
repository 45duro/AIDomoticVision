import requests
import json


subscription_key = 'b0655492a6224e5f8b272d92cbd1138c'
assert subscription_key

face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'

image_url = 'https://lh3.googleusercontent.com/7bhxO9aoPM0ilfaUwToYxNxsFBWDyl15Tb6x-wcFvOlxOSGE0AKCYVm5crCeb3I8vZVMkPU5TDAdKvznzzZsATwAeA8psEo0chchGYcUjXs9-SodTNZsVzfsLCt7afmz02--c0CNOqwd0Acm5owwhbf6P5ko0j5IlKFgxogyD-CxaPLve2pBMTZWyeNIHhQeD1a563dGf1P7qY5QYuCjFWIkXy1A-p-j4BlrVnk6_ryz2k3Wqqz1P3UED13HYjIJbxKv1TM2mghEXAzKjhtRdKSH_FMZhkbR6nlU2qOzAHnBJLlyfWQST7ESj5BqsOezKUkjecxTE5LfkteR88H5CGZTtIukVNqDodCHPEn_U1O7PBfFPjMuI2zLyWf8NIe6mfYY-2-xEqSez8dFxOfvdf5-FHTf7iQwtgLpVkM3bxUl7Tg_Ozo1V8nIgbsRcytueaxqUvACE_lLaw1iFAovVJHQ4qqYcPTEilGWNR9Kgj5SN4vBzQY4dFbCRtaE_i4xzBOaB0Utrn-2Ew3KPDmf_UKSBZYJjP3QONLGOxvNFuXD6BTePmDhF96OPukvaej8egmht-ZoRXJdSQLXDH2P-o8qajBbx0tIeZZq-yewzrZ12_X9HxnXc4cVid4zmgJ-FGAOT9pFqF4Y_mpJ2b4INSGFTJISAfVTntXxtk9PmpO-uAslp71PzCJd_OwtlmSabMBwdWtSOfmRjCDJJGLuGIQq=w876-h657-no'

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
    
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'recognitionModel': 'recognition_02',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_01',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
print(json.dumps(response.json()))

