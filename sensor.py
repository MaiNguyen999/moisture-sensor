from machine import ADC,Pin
import time

class Sensor:
    def __init__(self):
        self._adc = ADC(Pin(36))
        self._adc.atten(ADC.ATTN_11DB)

    def moisture(self):
        raw = self._adc.read()
        percent = "{:.2%}".format( raw / 4095)
        volts = "{:.3f}V".format(3.3 * raw / 4095)
        timestamp = time.localtime()
        formattedTime = "{0}-{1}-{2} {3}:{4}:{5}".format(timestamp[0],timestamp[1],timestamp[2],timestamp[3] - 5,timestamp[4],timestamp[5])
        return {"state":{
            "reported": {
                "raw": raw,
                "percent": percent,
                "volts": volts,
                "timestamp":formattedTime
                }
            }
        }