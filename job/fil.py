from microbit import *
import radio

# Virker en radio hvis den ikke er på?
radio.on()

radio.config(group=213)

# Luuuup
while True:
    pos = radio.receive()
    if pos:
        display.clear()
        x,y=pos.split(',')
        display.set_pixel(int(x),int(y),9)
        

