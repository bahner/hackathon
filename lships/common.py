from microbit import display, button_a, button_b
import radio
import random

# INIT
players =  {}

radio.config(group=213)
radio.on()

def parse_init_msg(msg):
    """Parse and use receive message"""
    key, value = msg.split(':')
    players[key] = value


def is_game_inited():
    """Evaluate whether or not game is Initialized properly"""

    # If any player has not seen all, then this is false
    for player in players:
        if players[player] < len(players):
            return False

    return True

# INIT gamers
def init_game():
    """Initialize game"""

    min_id = random.randint(0, 10000000)
    parse_init_msg("%s:%s" % (min_id, 1))

    while True:
        # If someone sends bogus data, then continue.
        try:
            msg = radio.receive().split(':')
        except ValueError:
            continue

        parse_init_msg(msg)
        display.show(players.get(min_id))
        # Use button a to
        if button_a.is_pressed():
            radio.send("%s:%s" % (min_id, len(players)))
        if button_b.is_pressed() and is_game_inited():
            break

    return players
