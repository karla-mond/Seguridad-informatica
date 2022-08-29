import secrets
from vigenere import vigenereCipher

def oneTimePad(message):
    message.lower();
    otp = ''
    for i in range(len(message)):
        otp += secrets.choice("abcdefghijklmnopqrstuvwxyz ")
    cipherMessage = vigenereCipher(otp, message)
    return otp, cipherMessage