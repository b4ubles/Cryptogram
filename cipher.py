from lib.encode.Bacon import Bacon
from lib.encode.Caesar import caesar
from lib.encode.Morse import morse_encode, morse_decode
from lib.encode.Fence import fence_encrypt, fence_decrypt
from lib.encode.Vigenere import Vigenere
from lib.crypt.RSA import RSA
from lib.crypt.AES import AES
from lib.crypt.Rabin import Rabin
from lib.crypt.polynomial import Polynomial


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
