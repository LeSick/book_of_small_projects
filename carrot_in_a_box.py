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

print(
    '''HERE ARE THE BOXES:
    ____________     ____________
   /           /|   /           /|
  +-----------+ |  +-----------+ |
  |    RED    | |  |    GOLD   | |
  |    BOX    | /  |    BOX    | /
  |           |/   |           |/
  +-----------+    +-----------+
/n
'''
)
print(player_names + '\n')
print(player_1_name + 'you have a RED box in front of you./n')
print(player_2_name + 'you have a GOLD box in front of you./n')
print()
print(player_1_name + ', you will get to look into your box./n')
print(player_2_name + ', you must close your eyes and look away!!! ))/n')
input(
    'When'
    + player_2_name
    + 'closes their eyes and looks away, press Enter.../n'
)
print(player_1_name + ', here is the inside of your box:/n')

if random.randint(1, 2) == 1:
    carrot_in_red_box: bool = True
else:
    carrot_in_red_box: bool = False
