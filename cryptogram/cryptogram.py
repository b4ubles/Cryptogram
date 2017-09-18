from encode.Bacon import Bacon
from encode.Caesar import caesar
from encode.Morse import morse_encode, morse_decode
from encode.Fence import fence_encode, fence_decode
from encode.Vigenere import Vigenere
from crypt.RSA import RSA
from crypt.AES import AES
from crypt.Rabin import Rabin
from crypt.polynomial import Polynomial
from information.Huffman import Huffman
from information.information_theory import entropy, Shanon, Fano


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
        except Exception, e:
            print e

if __name__ == '__main__':
    main()
