import hmac
import hashlib
from binascii import a2b_hex


def generate_hotp(c):
    key = bytes.fromhex('87c0312c4dc7fe2ef577871f13db76e547152f50')
    hash = hmac.digest(key, c, hashlib.sha1)
    s = hash
    i = s[19] & 0xf
    b = ((s[i] << 24) | (s[i + 1] << 16) | (s[i + 2] << 8) | (s[i + 3] << 0)) & 0x7FFFFFFF
    print("B: " + str(b))
    oath = 'unbu58550402'
    otp = str(b % 10 ** 6).zfill(6)
    print("OTP: " + otp)
    return oath + otp


if __name__ == '__main__':

    counter = '0000000000000000'
    while True:
        print('Counter: ' + counter)
        hotp = generate_hotp(a2b_hex(counter))
        print(hotp)
        counter = str(int(counter) + 1).zfill(16)
        user_input = input("Nächster Key? | y / n : ")
        if user_input == 'y':
            continue
        elif user_input == 'n':
            break
