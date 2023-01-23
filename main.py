import string
import ex5
import os
from ex5 import CaesarCipher, VigenereCipher


if __name__ == '__main__':
    # caesar_cipher = CaesarCipher(3)
    # text = "Mtm is the BEST!"
    # encrypted_text = caesar_cipher.encrypt(text)
    # decrypted_text = caesar_cipher.decrypt(encrypted_text)
    # print(text, encrypted_text, decrypted_text)
    # vigenere_cipher = VigenereCipher([7, 8, 11, 13, -2, 4])
    # text = "come to Rivendell!"
    # encrypted_text = vigenere_cipher.encrypt(text)
    # decrypted_text = vigenere_cipher.decrypt(encrypted_text)
    # print(text, encrypted_text, decrypted_text)

    # for file in os.listdir(path):
    #     file_path = os.path.join(path, file)
    #     if os.path.isfile(file_path):
    #         with open(file_path, 'r’) as f:
    #         print(f.read())
    #
    # Check valid(or exist) Config??? Exceptions???
    # Check if cipher valid in helper???
    path = "C:\\Users\\Gal\\Documents\\C C++\\ex5_test"
    ex5.processDirectory(path)

