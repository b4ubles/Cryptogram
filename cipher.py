from lib.Bacon import Bacon
from lib.Caesar import caesar
from lib.Morse import morse_encode, morse_decode
from lib.Fence import fence_encrypt, fence_decrypt
from lib.Vigenere import Vigenere
from lib.RSA import RSA
from lib.AES import AES
from lib.Rabin import Rabin


def console_print():
    print "+---------------------------------------------------------+"
    print "|                   Cipher Console                        |"
    print "+---------------------------------------------------------+"
    print "have fun with Bacon/caesar/Morse/Fence/RSA/Rabin here"


def main():
    console_print()
    while True:
        try:
            print '>>>', input()
        except Exception , e:
            print e
            
if __name__ == '__main__':
    main()
