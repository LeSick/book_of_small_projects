import random


NUM_DIGITS = 3
MAX_GUESS = 10


def main():
    print(
        f'''I am thinking of a {NUM_DIGITS}-digit with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:   That means:
    Pico          One digit is correct but in the wrong position.
    Fermi         One digit is correct and in the right position.
    Bagels        No digit is correct.

For example, if the secret numer was 248 and your guess was 843, the
clues would be Fermi Pico'''
    )

    while True:
        secret_number = get_secret_num()
        print('I have thought a number')
        print(f'You have {MAX_GUESS} guesses to get it.')

        num_guesses: int = 1
        while num_guesses <= MAX_GUESS:
            guess: str = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            if guess == secret_number:
                break
            if num_guesses > MAX_GUESS:
                print('You ran out of guesses.')
                print(f'The answer was {secret_number}')

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')


def get_secret_num() -> str:
    '''Returns a string made up of NUM_DIGITS unique random digits'''
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number: str = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess: str, secret_number: str) -> str:
    '''Reeturns a string with the pico, fermi, bagels clues
    for guess and secret number pair.
    '''
    if guess == secret_number:
        return 'You got it!'

    clues: list = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main()
