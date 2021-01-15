from umqtt.simple import MQTTClient
from sensor import Sensor
from machine import Timer
import json
#setup AWS SSL
KEY_PATH = "aad2ef0d0f-private.pem.key"
CERT_PATH = "aad2ef0d0f-certificate.pem.crt"
mySensor=Sensor()
try:
    with open(KEY_PATH,"r") as f:
        key = f.read()
    with open(CERT_PATH,"r") as f:
        cert = f.read()
except Exception as e:
    print("ReadSSL Certs",e)

#setup AWS parameters
CLIENT_ID = "331e7489-26ee-4755-8ee0-4d849e5240e1"
HOST = "a3ubtgymfu1sxe-ats.iot.ca-central-1.amazonaws.com"
PORT = 8883
SSL_PARAMS = {"key":key, "cert": cert, "server_side":False}

#setup MQTT
try:
    global client
    client = MQTTClient(client_id=CLIENT_ID,
                        server=HOST,
                        port=PORT,
                        keepalive=10000,
                        ssl=True,
                        ssl_params=SSL_PARAMS)
    client.connect()
    print("Sucessfully connected to AWS")
except Exception as e:
    print("Setup MQTT Error",e)


def publish_data(obj):
    data = mySensor.moisture()
    client.publish("$aws/things/Firebeetle/shadow/update",json.dumps(data))
    client.publish("$aws/things/Firebeetle/shadow/get",json.dumps({}))

tmr = Timer(-1)
tmr.init(mode=Timer.PERIODIC, period=60000, callback=publish_data)