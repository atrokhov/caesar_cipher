require_relative "caesar_cipher"
require "test/unit"

class TestCipher < Test::Unit::TestCase

    def test_with_string_alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        string = "The quick brown fox jumps over the lazy dog"

        shifts = [3, 5, 18, 25, 33]
        encoded_strings = ["Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj", "Tmj vznhp gwtbs ktc ozrux tajw ymj qfed itl", "Tzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy", "Tgd pthbj aqnvm enw itlor nudq sgd kzyx cnf", "Tol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"]

        shifts.size.times do |i|
            assert_equal(encoded_strings[i], CesarCipher.new(alphabet, shifts[i]).encode(string))
        end
    end

    def test_with_array_alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz".split("")
        string = "The quick brown fox jumps over the lazy dog"

        shifts = [3, 5, 18, 25, 33]
        encoded_strings = ["Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj", "Tmj vznhp gwtbs ktc ozrux tajw ymj qfed itl", "Tzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy", "Tgd pthbj aqnvm enw itlor nudq sgd kzyx cnf", "Tol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"]

        shifts.size.times do |i|
            assert_equal(encoded_strings[i], CesarCipher.new(alphabet, shifts[i]).encode(string))
        end
    end

end