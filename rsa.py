
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

def rsa_encrypt(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

plaintext = b'This is a secret message.'

public_key = key.publickey()
encrypted_data = rsa_encrypt(plaintext, public_key)
print("Encrypted:", encrypted_data)

private_key = key
decrypted_data = rsa_decrypt(encrypted_data, private_key)
print("Decrypted:", decrypted_data.decode())
