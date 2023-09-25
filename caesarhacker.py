''' Caesar Cipher Hacker programm
Hacks encrypted messages made of
ABCDEFGHIJKLMNOPQRSTUVWXYZ symbols
'''
from typing import Final

# Let the user specify the message to hack
print('Please, enter the encrypted message to hack:')
message = input('> ')

SYMBOLS: Final = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num: int = SYMBOLS.find(symbol)
            num -= key

            if num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]
        else:
            translated += symbol

    print(f'Key {key}: {translated}')
