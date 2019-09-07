import unittest
from caesar_cipher import *


class TestSum(unittest.TestCase):

    def test_with_string_alphabet(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        string = "The quick brown fox jumps over the lazy dog"

        shifts = [3, 5, 18, 25, 33]
        encoded_strings = ["Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj", "Tmj vznhp gwtbs ktc ozrux tajw ymj qfed itl", "Tzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy", "Tgd pthbj aqnvm enw itlor nudq sgd kzyx cnf", "Tol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"]

        cipher = CesarCipher()
        cipher.set_alphabet(alphabet)

        for i in range(0, len(shifts)):
            cipher.set_shift(shifts[i])
            self.assertEqual(cipher.encode(string), encoded_strings[i])

    def test_with_list_alphabet(self):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        string = "The quick brown fox jumps over the lazy dog"

        shifts = [3, 5, 18, 25, 33]
        encoded_strings = ["Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj", "Tmj vznhp gwtbs ktc ozrux tajw ymj qfed itl", "Tzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy", "Tgd pthbj aqnvm enw itlor nudq sgd kzyx cnf", "Tol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"]

        cipher = CesarCipher()
        cipher.set_alphabet(alphabet)

        for i in range(0, len(shifts)):
            cipher.set_shift(shifts[i])
            self.assertEqual(cipher.encode(string), encoded_strings[i])

if __name__ == '__main__':
    unittest.main()