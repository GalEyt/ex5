import string


class CaesarCipher:
    LOWERCASE_ALPHABET = string.ascii_lowercase
    UPPERCASE_ALPHABET = string.ascii_uppercasecase
    NUM_OF_LETTERS = len(LOWERCASE_ALPHABET)

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        encrypted = []
        for letter in plaintext:
            if letter.isupper():
                encrypted.append(UPPERCASE_ALPHABET[])


