# -*- coding: utf-8 -*-
# @author Lyle
# version 6-14

import unittest
from information_theory import *
from Huffman import *


class InformationTheoryTest(unittest.TestCase):

    def test_entropy(self):
        self.assertEqual(entropy([0.5, 0.5]), 1)
        self.assertEqual(entropy([1/8.0, 1/8.0, 0.25, 0.5]), 1.75)

    def test_Shanon(self):
        self.assertEqual(
            Shanon([0.01, 0.1, 0.15, 0.17, 0.18, 0.19, 0.2]),
            ['000', '001', '011', '100', '101', '1110', '1111110'])
        self.assertEqual(
            Shanon([0.05, 0.25, 0.10, 0.15, 0.20, 0.25]),
            ['00', '01', '100', '101', '1101', '11110'])

    def test_Fano(self):
        self.assertEqual(
            Fano([0.32, 0.22, 0.18, 0.16, 0.08, 0.04]),
            ['00', '01', '10', '110', '1110', '1111'])
        self.assertEqual(
            Fano([0.01, 0.1, 0.15, 0.17, 0.18, 0.19, 0.2]),
            ['00', '010', '011', '10', '110', '1110', '1111'])

    def test_Huffman(self):
        self.assertEqual(
            Huffman({'a': 0.01, 'b': 0.1, 'c': 0.15,
                     'd': 0.17, 'e': 0.18, 'f': 0.19, 'g': 0.2}).encode,
            {'a': '0111', 'c': '010', 'b': '0110', 'e': '000',
             'd': '001', 'g': '10', 'f': '11'})
        self.assertEqual(
            Huffman({'a': 0.4, 'c': 0.1, 'b': 0.18, 'e': 0.07,
                     'd': 0.1, 'g': 0.05, 'f': 0.06, 'h': 0.04}).encode,
            {'a': '1', 'c': '0000', 'b': '001', 'e': '0100',
             'd': '011', 'g': '00010', 'f': '0101', 'h': '00011'})


if __name__ == '__main__':
    unittest.main()
