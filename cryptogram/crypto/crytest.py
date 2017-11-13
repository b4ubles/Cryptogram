#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cryptography import *

# string used to test encrypt
TESTCASE = "19359591402132342894798"
TESTCASE += "阿姆斯特朗回旋加速喷气式阿姆斯特朗炮"
TESTCASE += "⊙﹏⊙→_→\(^o^)/"
TESTCASE += "αΓвбЕΤусфоНМЛ㈕ㅂㄳㅌㅄㅣゲフテケ"
'''
TESTCASE += "sahkjshhsahdkjjsanjh"
TESTCASE += "!@#~!@#$ &^^&&  %*()(&_{:< >?<> "
TESTCASE += "<?//.,|\\2333I;M"
'''


class CryptTest(unittest.TestCase):

    def test_congruence(self):
        self.assertEqual(
            congruence(33, 22, 77),
            [10, 17, 24, 31, 38, 45, 52, 59, 66, 73, 3])

    def test_Euclidean(self):
        self.assertEqual(Euclidean(737, 635), [193, -224])
        with self.assertRaises(TypeError):
            Euclidean(737, 635.0)
        with self.assertRaises(TypeError):
            Euclidean(737, '635.0')
        with self.assertRaises(ValueError):
            Euclidean(-737, 635)

    def test_Legendre(self):
        self.assertEqual(Legendre(2, 59), -1)
        self.assertEqual(Legendre(137, 227), -1)
        self.assertEqual(Legendre(41, 2000000000000000000000000029967), 1)
        self.assertEqual(Legendre(71, 2000000000000000000000000029967), -1)
        self.assertEqual(Legendre(41, 20000000000000000000000000037023), 1)
        self.assertEqual(Legendre(71, 20000000000000000000000000037023), -1)
        self.assertEqual(Legendre(31, 2**192 - 2**64 - 1), -1)
        self.assertEqual(Legendre(79, 2**192 - 2**64 - 1), 1)

    def test_mrsm(self):
        self.assertEqual(mrsm(12996, 227, 37909), 7775)
        self.assertEqual(mrsm(312, 13, 667), 468)
        self.assertEqual(mrsm(501, 13, 667), 163)
        self.assertEqual(mrsm(468, 237, 667), 312)
        self.assertEqual(mrsm(163, 237, 667), 501)

    def test_ordam(self):
        self.assertEqual(ordam(4, 7), 3)
        self.assertEqual(ordam(9, 14), 3)
        self.assertEqual(ordam(8, 15), 4)

    def test_primeFactor(self):
        self.assertEqual(set(primeFactor(293891, True)), set([13, 37, 47]))
        self.assertEqual(primeFactor(293891), [13, 13, 37, 47])
        self.assertEqual(primeFactor(29389), [29389])

    def test_primitiveRootList(self):
        self.assertEqual(primitiveRootList(17), [3, 5, 6, 7, 10, 11, 12, 14])
        self.assertEqual(primitiveRootList(100), [])
        self.assertEqual(primitiveRootList(151),
                         [6, 7, 12, 13, 14, 15, 30, 35, 48, 51, 52,
                          54, 56, 61, 63, 71, 77, 82, 89, 93, 96, 102,
                          104, 106, 108, 109, 111, 112, 114, 115, 117,
                          120, 126, 129, 130, 133, 134, 140, 141, 146])

if __name__ == '__main__':
    unittest.main()
