from microbit import *
from lships.common import init_game

# Initialize the player
players = init_game()
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
