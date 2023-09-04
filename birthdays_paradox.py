import datetime
import random

from typing import List


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def get_birthdays(number_of_birthdays: int) -> List:
    '''Reterns a list of numbers random date objects for birthdays.'''
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays: List) -> None or datetime:
    '''Returns the date object of a birthday
    that occurs more than once on the birthdays list
    '''
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


print('''The Birthday Paradox shows us that in a group of
N people, the odds that two of them have matching birthdays
is surprisingly large. This program does a Monte Carlo simulation
(that is, repeated random simulation) to explore this concept.

(It's not actualy a paradox, it's just a surprising result.)
''')

while True:
    print("Hoe many birthdays shall I generate? (max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

print(f'Here are {num_bdays} birthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = f'{month_name} {birthday.day}'
        print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print('multiply people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')
print()

print(f'Generating {num_bdays} random birthdays 100 000 times...')
input('Press Enter to begin...')
print('Let\'s run 100 000 simulations.')
sim_match = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) is not None:
        sim_match += 1
print('100 000 simulations run.')

proba = round(sim_match / 100_000 * 100, 2)
print(f'Out of 100 000 simulations of {num_bdays} people, there was a')
print(f'matching birthday in that group {sim_match} times. This means')
print(f'that {num_bdays} people have a {proba}% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
