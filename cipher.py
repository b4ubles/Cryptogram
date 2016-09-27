from lib.Bacon import Bacon
from lib.Caesar import caesar
from lib.Morse import Morse_decode, Morse_encode
from lib.Fence import fence_encrypt, fence_decrypt
from lib.Vigenere import Vigenere


def console_print():
    print "+------------------------+"
    print "|     Cipher Console     |"
    print "+------------------------+"


def main():
    console_print()
    while True:
        print '>>>', input()

if __name__ == '__main__':
    main()
