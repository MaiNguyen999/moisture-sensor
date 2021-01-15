import paho.mqtt.client as mqtt
import ssl
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)
    client.subscribe("$aws/things/Firebeetle/shadow/get/accepted")

def on_message(client, userdata, msg):
    myData = json.loads(msg.payload)
    moistureData = myData['state']['reported']
    print("-------------------------------------------------")
    print("Raw: {0} @ {1}".format(moistureData['raw'], moistureData['timestamp']))
    print("Percent: {0} @ {1}".format(moistureData['percent'],moistureData['timestamp']))
    print("Voltage: {0} @ {1}".format(moistureData['volts'],moistureData['timestamp']))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs="AmazonRootCA1.pem",
                certfile="aad2ef0d0f-certificate.pem.crt",
                keyfile="aad2ef0d0f-private.pem.key",
                cert_reqs=ssl.CERT_REQUIRED,
                tls_version=ssl.PROTOCOL_TLS,
                ciphers=None
                )

client.connect("a3ubtgymfu1sxe-ats.iot.ca-central-1.amazonaws.com", 8883, 60)
client.loop_forever()