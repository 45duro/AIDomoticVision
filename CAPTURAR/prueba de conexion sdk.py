
from iothub_client import IoTHubClient, IoTHubTransportProvider, IoTHubMessage
import time

CONNECTION_STRING="HostName=tecnobotIoT.azure-devices.net;DeviceId=Raspi;SharedAccessKey=7qPwpj8r/p3FI7oiRGJluC/W4wQxJdiqoQPOBcN875I="
PROTOCOL = IoTHubTransportProvider.MQTT


def send_confirmation_callback(message, result, user_context):
    print("Confirmation received for message with result = %s" % (result))

def dataTemp():

    return random.uniform(0, 10)


def send_message(token, message):
    #url = 'https://{0}/devices/{1}/messages/events?api-version=2016-11-14'.format(URI, IOT_DEVICE_ID)
    url = 'https://{0}/devices/{1}/messages/events?api-version=2018-06-30'.format(URI, IOT_DEVICE_ID)
    print(token)
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
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    message = IoTHubMessage("test message")
    client.send_event_async(message, send_confirmation_callback, None)
    print("Message transmitted to IoT Hub")

    while True:
        time.sleep(1)