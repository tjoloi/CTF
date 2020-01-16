if __name__ == '__main__':
    print('Welcome to the RootMe python crackme')
    PASS = 'ŊŞŧŮŵŢŞőŖŅŚŞĠĞĢ'
    KEY = 'I know, you love decrypting Byte Code !'
    I = 5
    SOLUCE = [57, 73, 79, 16, 18, 26, 74, 50, 13, 38, 13, 79, 86, 86, 87]
    KEYOUT = []
    for X in PASS:
        KEYOUT.append((ord(X) + I ^ ord(KEY[I])) % 255)
        print(I)
        I = (I + 1) % len(KEY)

    print(KEYOUT)
    if SOLUCE == KEYOUT:
        print('You Win')
    else:
        print('Try Again !')