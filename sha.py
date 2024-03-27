
import hashlib

def sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.digest()

data = b'This is some data to hash.'

hashed_data = sha256_hash(data)
print("Hashed data (SHA-256):", hashed_data.hex())
