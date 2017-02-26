# coding: utf-8
"""Lage en skipsradio (VHF)"""
from microtbit import *
from radio
import random

class Radio(object):
    """Sender signaler mellom skip
    """

    def __init__(self,
                 gruppe=213,
                ):

        """Init radio"""

        self._id = random.randint(10)
        radio.on()


    def status(self):
        """Give status of object"""
        ret = {
            'nummer': self._id,
            'eier': self.eier,
        }

        return ret
