from microbit import *

foo = Image.HAPPY
bilde = Image(10,10)
x = 0

while True:
    if button_a.is_pressed():
        x = x - 1
    elif button_b.is_pressed():
        x = x + 1
    bilde.blit(foo, 0, 0, 4, 4, xdest=x, ydest=0)
    display.show(bilde)
    sleep(1)
