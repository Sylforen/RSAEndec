import argparse
from sympy import mod_inverse

stringToBeHashed1 = "ABCDEFG"
stringToBeHashed2 = "1234567"

prime1 = 23
prime2 = 29

n = prime1 * prime2
phi = (prime1 - 1) * (prime2 - 1)
e = 3
d = mod_inverse(e, phi)

def main():
    parser = argparse.ArgumentParser(description="Hash and decrypt strings.")
    parser.add_argument(
        "--string", "-s", type=str, default=stringToBeHashed1, help="String to be hashed"
    )
    args = parser.parse_args()

    stringToBeHashed = args.string

    print(f"\nRaw data is: {stringToBeHashed}")
    encrypted = rsa_encrypt(stringToBeHashed)
    print(f"Encrypted data is: {encrypted}")
    decrypted = rsa_decrypt(encrypted)
    print(f"Decrypted data is: {decrypted}")

def rsa_encrypt(string):
    encrypted_list = [pow(ord(char), e, n) for char in string]
    return encrypted_list

def rsa_decrypt(encrypted_list):
    decrypted_list = [chr(pow(char, d, n)) for char in encrypted_list]
    return ''.join(decrypted_list)

if __name__ == "__main__":
    main()