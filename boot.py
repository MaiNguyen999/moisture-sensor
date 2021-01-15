import time
import network
import webrepl
from ntptime import settime

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('SHAW-A3FB60','251154007409')
        while not wlan.isconnected():
            wlan.connect('SHAW-A3FB60','251154007409')
            time.sleep(5)
        print('Network config: ', wlan.ifconfig())

do_connect()
settime()
webrepl.start()
