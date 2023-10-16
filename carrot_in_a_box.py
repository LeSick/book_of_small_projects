import os
import random


print(
    '''Carrot in a Box, by Al Sweigart

    This is a bluffing game for two players. Each player has a box.
    One box has a carrot in it. To win, you must have the box with the
    carrot in it.

    This is very simple and silly game.

    The first player looks into their box (the second player must close
    their eyes during this). The first player then says "There is a carrot
    in my box" or "There is not a carrot in my box". The second player then
    gets to decide if they want to swap boxes or not.
'''
)
input('Press Enter to begin...')

player_1_name: str = input('Human Player 1, enter your name: ')
player_2_name: str = input('Human Player 2, enter your name: ')
player_names: str = (
    player_1_name[:11].center(11) +
    '   ' + player_2_name[:11].center(11)
)

print('''HERE ARE THE BOXES:
    ____________     ____________
   /           /|   /           /|
  +-----------+ |  +-----------+ |
  |    RED    | |  |    GOLD   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
'''
)
print(player_names + '\n')
print(player_1_name + ', you have a RED box in front of you.\n')
print(player_2_name + ', you have a GOLD box in front of you.\n')
print()
print(player_1_name + ', you will get to look into your box.\n')
print(player_2_name + ', you must close your eyes and look away!!! ))\n')
input(
    'When '
    + player_2_name
    + ' closes their eyes and looks away, press Enter...\n'
)
print(player_1_name + ', here is the inside of your box:\n')

if random.randint(1, 2) == 1:
    carrot_in_first_box: bool = True
else:
    carrot_in_first_box: bool = False

if carrot_in_first_box:
    print('''
     ____VV_____
    |    VV     |
    |    VV     |
    |____||_____|    ____________
   /     ||    /|   /           /|
  +-----------+ |  +-----------+ |
  |    RED    | |  |    GOLD   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
   (carrot!!!)
'''
)
    print(player_names)
else:
    print('''
     ___________
    |           |
    |           |
    |___________|    ____________
   /           /|   /           /|
  +-----------+ |  +-----------+ |
  |    RED    | |  |    GOLD   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
  (no carrot!!!)
'''
)
    print(player_names + '\n')

input('Press Enter to continue...')

os.system('clear')
print(player_1_name + ', tell ' + player_2_name + ' to open their eyes.')
input('Press Enter to continue...')

print()
print(
    player_1_name + ', say one of the following sentences to '
    + player_2_name + '.'
)
print(' 1) There is a carrot in my box.')
print(' 2) There is no carrot in my box.')
print()
input('Press Enter to continue...')

print()
print(
    player_2_name + ', do you want to swap boxes with '
    + player_1_name + '? YES/NO'
)
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(player_2_name + ', please, enter "Yes" or "NO".')
    else:
        break

first_box: str = 'RED'
second_box: str = 'GOLD'

if response.startswith('Y'):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box

print(f'''HERE ARE THE BOXES:
    ____________     ____________
   /           /|   /           /|
  +-----------+ |  +-----------+ |
  |    {first_box}    | |  |    {second_box}   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
'''
)
print(player_names)

input('Press Enter to reveal the winner...')
print()

if carrot_in_first_box:
    print(f'''
     ____VV_____     ____________
    |    VV     |   |            |
    |    VV     |   |            |
    |____||_____|   |____________|
   /     ||    /|   /           /|
  +-----------+ |  +-----------+ |
  |    {first_box}   | |  |    {second_box}   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
'''
)
else:
    print(f'''
     ___________     _____VV_____
    |           |   |     VV     |
    |           |   |     VV     |
    |___________|   |_____||_____|
   /           /|   /     ||    /|
  +-----------+ |  +-----------+ |
  |    {first_box}   | |  |    {second_box}   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
'''
)
    print(player_names)

# This modification made possible
# through the 'carrot_in_first_box' variable
if carrot_in_first_box:
    print(player_1_name + ' is the winner!')
else:
    print(player_1_name + ' is the winner!')
print('Thank you for playing!')
