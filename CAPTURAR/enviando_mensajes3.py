import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess
from base64 import b64encode, b64decode
from hashlib import sha256
import hmac as HMAC
import json
import time
import urllib.request
import urllib.parse
import requests
import random

URI= 'tecnobotIoT.azure-devices.net'
KEY= 'WoLMCYfNuTiaV8nCPdga98vU2uItTXzqUzCYN8qy3hw='
IOT_DEVICE_ID='Raspi'
POLICY='iothubowner'

def generate_sas_token():
    expiry=3600
    ttl = time.time() + expiry
    sign_key = "%s\n%d" % (urllib.parse.quote_plus(URI), int(ttl))

    #con b64decode(sign_key) en el segundo argumento varia el token
    #con None en el segundo siempre queda igual
    flag = b64decode(sign_key)
    digest_maker = HMAC.new(b64decode(KEY), flag, sha256)
    signature = b64encode(digest_maker.digest())
    
    rawtoken = {
        'sr' :  URI,
        'sig': signature,
        'se' : str(int(ttl))
    }

    rawtoken['skn'] = POLICY

    

    return 'SharedAccessSignature ' + urllib.parse.urlencode(rawtoken)


def dataTemp():

    return random.uniform(0, 10)


def send_message(token, message):
    url = 'https://{0}/devices/{1}/messages/events?api-version=2016-11-14'.format(URI, IOT_DEVICE_ID)
    #url = 'https://fully-qualified-iothubname.azure-devices.net/devices/{1}/messages/events?api-version=2018-06-30'.format(URI, IOT_DEVICE_ID)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = json.dumps(message)
    #print(data)
    response = requests.post(url, data=data, headers=headers)

def ImagenTomada():
    return "https://tecnobotstorage.blob.core.windows.net/fotos/humo10.jpg"

if __name__ == '__main__':

    # 1. Enable  Sensor


    # 2. Generate SAS Token
    token = generate_sas_token()
    
    
    # 3. Send fotos y datos al IoT Hub

    data = []#Para hacer el json
    flag = True
    for i in range(0,200,1):
        temp = dataTemp()
        tiempoactual = str(time.strftime("%c"))
        message = { 
            "deviceId": IOT_DEVICE_ID,
            "temp": temp,
            "latitude": 4.437069,
            "longitude": -75.202319,
            "url": ImagenTomada(),
            "timestamp": tiempoactual,
            "EventProcessedUtcTime": tiempoactual,
            "PartitionId": 1,
            "EventEnqueuedUtcTime": tiempoactual,
            "IoTHub": {
                "MessageId": "null",
                "CorrelationId": "null",
                "ConnectionDeviceId": "Raspi",
                "ConnectionDeviceGenerationId": "636494537606587154",
                "EnqueuedTime": "tiempoactual",
                "StreamId": "null"
            }
        }
        send_message(token, message)

        #Agregar al registro
        data.append(message)
        time.sleep(0.5)

        # sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample application will exit.")
        # sys.stdout.flush()
        # flag = input()
        # if(flag != 1):
        #     break

        
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)