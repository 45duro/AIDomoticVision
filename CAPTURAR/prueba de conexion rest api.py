
URI= 'tecnobotIoT.azure-devices.net'
KEY= 'WoLMCYfNuTiaV8nCPdga98vU2uItTXzqUzCYN8qy3hw='
IOT_DEVICE_ID='Raspi'

url = 'https://{0}/devices/{1}/messages/events?api-version=2016-11-14'.format(URI, IOT_DEVICE_ID)
url = 'https://fully-qualified-iothubname.azure-devices.net/devices/{1}/messages/events?api-version=2018-06-30'.format(URI, IOT_DEVICE_ID)
print(url)

