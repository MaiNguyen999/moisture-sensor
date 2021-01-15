# moisture-sensor
This project uses AWS IOT, ESP32 Firebeetle and a soil moisturizer to send raw moisture level, percentage and voltage every 60 seconds to the client.

## Boot.py
This file will be loaded to the ESP32. It will be the very first file ran when ESP32 is booted.

## Main.py
This file will be loaded to the ESP32. This is the next file ran after boot file. The main function of this file is to connect with AWS IOT and send moisture informations to AWS every minute.

## Mqtt-Client.py
This file is ran on local machine. It will listen to /shadow/get and display moisture information on command prompt.



