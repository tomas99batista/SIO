# 3DES
# AES-128
# ChaCha20
import getpass, os, base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def derive_key(password):
    backend=default_backend()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        lenght=32,
        salt=salt,
        iterations=100000,
        backend=backend)
    
    key = kdf.derive(password.encode('utf-8'))
    return salt, key

password = getpass.getpass()
salt, key = derive_key(password)
print("Password: {} | Salt: {} | Key: {}".format(password, salt, key))

# Vai devovler texto criptogrado
def sym_encrypter(key, algorithm, text):
    if algorithm == 'AES':
        algor = algorithms.AES(key)
    elif algorithm == '3DES':
        algor = algorithms.DES3(key)
    elif algorithm == 'ChaCha20':
        algor = algorithms.ChaCha20(key)
    else:
        raise(Exception("Invalid algorithm"))
    
    bs = algor.block_size / 8
    missing_bytes = bs - len(text) % bs
    if missing_bytes == 0:
        missing_bytes = 16
    
    padding = bytes([missing_bytes] * missing_bytes)
    text += padding
    print("Text + Padding: {}".format(text))
    
    cipher = Cipher(algor, modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    cryptogram = encryptor.update(text) + encryptor.finalize()
    
    return cryptogram
  
# Decriptaçao vai devolver o texto que estava criptogrado
def sym_decrypter(key, algorithm, cryptogram):
    if algorithm == 'AES':
        algor = algorithms.AES(key)
    elif algorithm == '3DES':
        algor = algorithms.DES3(key)
    elif algorithm == 'ChaCha20':
        algor = algorithms.ChaCha20(key)
    
    cipher = Cipher(algor, modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    text = decryptor.update(text) + decryptor.finalize()
    
    return text
