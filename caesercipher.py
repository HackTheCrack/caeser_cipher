import pyperclip

message = input("please enter the string: ")

key = int(input("Enter keysize: "))

mode = input("please specify encrypt or decrypt: ")

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
    
print(translated)

pyperclip.copy(translated)