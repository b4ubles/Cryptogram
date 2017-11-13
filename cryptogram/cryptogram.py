#!/usr/bin/env python
# -*- coding: utf-8 -*-

from encode.Bacon import Bacon
from encode.Caesar import caesar
from encode.Morse import morseEncode, morseDecode
from encode.Fence import fenceEncode, fenceDecode
from encode.Vigenere import Vigenere
from crypt.RSA import RSA
from crypt.AES import AES
from crypt.Rabin import Rabin
from crypt.polynomial import Polynomial
from information.Huffman import Huffman
from information.information import entropy, Shanon, Fano


def main():
    print "+---------------------------------------------------------+"
    print "|                   Cipher Console                        |"
    print "+---------------------------------------------------------+"
    print "have fun with Bacon/caesar/Morse/Fence/RSA/Rabin here"
    while True:
        try:
            print '>>>', input()
        except Exception, e:
            print e

if __name__ == '__main__':
    main()
