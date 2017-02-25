from microbit import *
import radio
import random

spillere = set()

radio.config(group=213)
radio.on()

def send_random_pos(vis=False):
    """Sender en ttildelfig posisjon
        Posisjonen blir opplyst lokalt
    """
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if vis:
        display.set_pixel(x, y, 5)
    radio.send("%s,%s" % (x, y))

min_id = random.randint(0, 10000)
spillere.add(min_id)

# INIT gamers
while True:
    msg = radio.recv():
    if msg:
        if msg == 'init':
            break
        else:
            spillere.add(msg)
        if button_a.is_pressed():
            radio.send(min_id)
        display.show(len(spillere))
    if button_b.is_pressed():
        for i in range(10):
            radio.send('init)
        break

while True:
    if button_a.is_pressed():
        display.clear()
        send_random_pos(vis=button_b.is_pressed())
    
