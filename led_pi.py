from gpiozero import LED
from time import sleep

led = LED(17)

while(1) :
    f = open("status.txt","r")
    status=f.read()
    if(status == '1'):
        led.on()
    elif(status == '0'):
        led.off()
    print status
    sleep(1)

