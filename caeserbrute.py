message = input('Please Enter The String: ')
    
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for ROT in range(len(LETTERS)):

    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - ROT

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol

    print('ROT #%s: %s' % (ROT, translated))