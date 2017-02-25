from microbit import *

foo = Image.SAD
display.show(foo)

while True:
    if button_a.is_pressed():
        foo = foo.shift_right(-1)
    elif button_b.is_pressed():
        foo = foo.shift_right(1)
    display.show(foo, clear=True)
    sleep(1)
