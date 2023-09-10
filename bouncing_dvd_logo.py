import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requiers the bext module.')
    print('You can install via: pip install Bext')
    sys.exit()

from typing import Final, Tuple, List


# Setup constants
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automaticlly, so reduce the width by one
WIDTH -= 1

NUMBER_OF_LOGOS: Final = 5
PAUSE_AMOUNT: Final = .2
COLORS: Final = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT: Final = 'ur'
UP_LEFT: Final = 'ul'
DOWN_RIGHT: Final = 'dr'
DOWN_LEFT: Final = 'dl'
DIRECTIONS: Tuple = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
# Key names for logo dictoinaries
COLOR: Final = 'color'
X: Final = 'x'
Y: Final = 'y'
DIR: Final = 'direction'


def main():
    bext.clear()

    # Generate some logos
    logos: List = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append(
            {COLOR: random.choice(COLORS),
             X: random.randint(1, WIDTH - 4),
             Y: random.randint(1, HEIGHT - 4),
             DIR: random.choice(DIRECTIONS)},
            )
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner
            logos[-1][X] -= 1

    corner_bounces: int = 0
    while True:
        for logo in logos:
            # Erase the logo's current location
            bext.goto(logo[X], logo[Y])
            print('  ', end='')

            original_direction = logo[DIR]

            # See if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces += 1

            # See if thr logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge
            # (WIDTH - 3) because 'DVD' has 3 letters
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != original_direction:
                # Change color when logo bounces
                logo[COLOR] = random.choice(COLORS)

            # Move the logo (X moves by 2 because the terminal
            # characters are twice as tall as they are wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corners bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corner_bounces, end='')

        for logo in logos:
            # Draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()
