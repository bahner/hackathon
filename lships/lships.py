# coding: utf-8
"""Beste massive multislagskip for Microbit"""
from microbit import *
import radio
import random


# Innstillinger
# spillerliste
spillere = {}

radio.config(group=213)
radio.on()


class Player(object):
    """En spiller

    Best�r hovedsakelig av et kart som det plasseres skip p�.
    """

    def __init__(self,
                 admiral,
                 xmax=4,
                 ymax=4):
        """Init map"""

        self._id = admiral
        self.xmax = xmax
        self.ymax = ymax
        self.map = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]

    def str(self):
        """Tekstrepresentasjon"""
        return str(self._id)

    def status(self):
        """Give status of object"""
        ret = {
            'owner': self._id,
            'map': self.map,
        }

        return ret

    def shoot(self):
        """Aims at a place"""

    def place_ship(self, ship):
        """Places a ship in the map"""

        # check that ship can be placed without overlapping
        for xpos, ypos in ship:
            if self.map[xpos][ypos]:
                return False

        for xpos, ypos in ship:
            self.map[xpos][ypos] = 9
        return True


def gen_incrementors():
    """Function decides on a direction to in-/decrement x and y

    If x and y are both zero one of the must yield, and redraw.
    """

    while True:
        _xpos = random.randint(-1, 1)
        _ypos = random.randint(-1, 1)
        if not _xpos and not _ypos:
            continue
        else:
            return (_xpos, _ypos)


def gen_start_pos(xmax, ymax):
    """Generates a point within the allow range to start drawing.
    """
    _xpos = random.randint(0, xmax)
    _ypos = random.randint(0, ymax)
    return (_xpos, _ypos)


def gen_ship(length, xmax, ymax):

    while True:
        hull = list()
        xpos, ypos = gen_start_pos(xmax, ymax)
        xinc, yinc = gen_incrementors()
        # Generate a ship
        for _ in range(0, length):
            hull = hull + [(xpos, ypos)]
            xpos = xpos + xinc
            ypos = ypos + yinc

        # Verify that it's not out of bounds.
        if not 0 <= xpos <= xmax:
            continue
        if not 0 <= ypos <= ymax:
            continue

        return hull


def parse_init_msg(msg):
    """Parse and use receive message"""
    key, value = str(msg).split(':')
    spillere[key] = value


def spillet_er_igang():
    """Evaluate whether or not game is Initialized properly"""

    # If any player has not seen all, then this is false
    for player in spillere:
        if spillere[player] < len(spillere):
            return False

    return True


# INIT gamers
def start_spill():
    """Initialize game"""

    min_id = random.randint(0, 10000000)
    spillere[min_id] = str(1)

    while True:
        # If someone sends bogus data, then continue.
        display.clear()
        msg = radio.receive()
        if isinstance(msg, str):
            parse_init_msg(msg)

        display.show(str(len(spillere)))
        # Use button a to
        if button_a.is_pressed():
            send_msg = "%s:%s" % (min_id, str(len(spillere)))
            radio.send(send_msg)
        if button_b.is_pressed() and spillet_er_igang():
            break

    return spillere


start_spill()
