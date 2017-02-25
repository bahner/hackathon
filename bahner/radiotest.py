from microbit import *
import radio
import uuid
import random
from lships.common import

# INIT
spillere = set()

radio.config(group=213)
radio.on()

# INIT gamers
def init_game():
    """Initialize game"""

    min_id = uuid.uuid4()
    spillere.add(min_id)

    while True:
        display.show(str(len(spillere)))
        msg = radio.receive()
        if msg:
            if msg == 'init':
                break
            else:
                spillere.add(msg)
        if button_a.is_pressed():
            radio.send(str(min_id))
        if button_b.is_pressed():
            for i in range(10):
                radio.send('init')
            break













while True:
    if button_a.is_pressed():
        display.clear()
        send_random_pos(vis=button_b.is_pressed())
    

def send_random_pos(vis=False):
    """Sender en ttildelfig posisjon
        Posisjonen blir opplyst lokalt
    """
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if vis:
        display.set_pixel(x, y, 5)
    radio.send("%s,%s" % (x, y))
