
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

plaintext = b'This is a secret message.'
key = get_random_bytes(16) 

encrypted_data = aes_encrypt(plaintext, key)
print("Encrypted:", encrypted_data)

decrypted_data = aes_decrypt(encrypted_data, key)
print("Decrypted:", decrypted_data.decode())
