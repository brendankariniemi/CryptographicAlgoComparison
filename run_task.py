import sys
import os
import psutil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def generate_key(length, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(os.urandom(length))


def encrypt_decrypt(file_path, algorithm, key_size):
    with open(file_path, 'rb') as file:
        data = file.read()
        file_size = file.tell()

    salt = os.urandom(16)
    key = generate_key(key_size // 8, salt)
    algo_class = getattr(algorithms, algorithm)
    if algorithm == 'ChaCha20':
        nonce = os.urandom(16)
        cipher = Cipher(algo_class(key=key, nonce=nonce), mode=None, backend=default_backend())
    else:
        iv_size = algo_class.block_size // 8
        iv = os.urandom(iv_size)
        cipher = Cipher(algo_class(key), modes.CFB(iv), backend=default_backend())

    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    process = psutil.Process(os.getpid())
    cpu_start = process.cpu_times()
    mem_start = process.memory_info()

    encrypted_data = encryptor.update(data) + encryptor.finalize()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    cpu_end = process.cpu_times()
    mem_end = process.memory_info()

    cpu_used = (cpu_end.user - cpu_start.user) + (cpu_end.system - cpu_start.system)
    memory_used = mem_end.rss - mem_start.rss

    print(f"{file_path},{file_size},{algorithm},{cpu_used},{memory_used}")


if __name__ == "__main__":
    encrypt_decrypt(sys.argv[1], sys.argv[2], int(sys.argv[3]))
