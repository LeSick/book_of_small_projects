try:
    import pyperclip
except ImportError:
    pass

SYMBOLS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(
    '''The Ceaser cipher encrypts letters by shifting them over by a
    key number. For example, a key of 2 means letter A is
    encrypted into C, the letter B iotn D, etc.
'''
)
print()

# Let the user enter if they are encrypting or decrypting
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode: str = 'encrypt'
        break
    elif response.startswith('d'):
        mode: str = 'decrypt'
        break
    print('Please, enter \'e\' or \'d\'')

while True:
    max_key: int = len(SYMBOLS) - 1
    print(f'Please, enter the key (0 to {max_key}) to use')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < max_key:
        key = int(response)
        break
# Let user enter the message to encrypt/decrypt
print(f'Enter the message to {mode}')
message: str = input('> ')

# Ceaser cipher only on uppercase letters
message = message.upper()

# Stores the encrypted/decrypted form of the message
translated: str = ''

# Encrypt/decript each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        num: int = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        else:
            num -= key
# Handle the wrap-around if num is larger than the length of
# SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')
except ImportError:
    pass
