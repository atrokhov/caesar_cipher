class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        encoded_text = ''
        alphabet = self._alphabet
        shift = self._shift

        for i in range(0, len(plainText)):
            if plainText[i] in alphabet:
                if alphabet.index(alphabet[alphabet.index(plainText[i])]) + shift >= len(alphabet):
                    shifted_index = alphabet.index(plainText[i]) + shift

                    while shifted_index >= len(alphabet):
                        shifted_index -= len(alphabet)

                    encoded_text += alphabet[shifted_index]

                else:
                    encoded_text += alphabet[alphabet.index(plainText[i]) + shift]
            else:
                encoded_text += plainText[i]
            
        return encoded_text
