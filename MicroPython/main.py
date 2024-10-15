"""
Created by: Gavin Gallant
Created on: Sep 2020
This program shows an If Statement
"""

from microbit import *
import random


display.clear()
display.show(Image.HAPPY)

while True:
    if accelerometer.was_gesture("shake"):
        random_number = random.randint(0, 2)
        display.clear()

        # if random_number was 0
        if random_number == 0:
            display.show(Image.SQUARE_SMALL)

        # if random_number was 1
        if random_number == 1:
            display.show(Image.SQUARE)

        # if random_number was 2
        if random_number == 2:
            display.show(Image ("99009:"
                                "99090:"
                                "00900:"
                                "99090:"
                                "99009"))

        # pause and show you are ready again
        sleep(1000)
        display.show(Image.HAPPY)


    if button_a.is_pressed():
        display.clear()
        score = score + 1
        display.show(Image.YES)
        display.clear()
        display.show(Image.HAPPY)






