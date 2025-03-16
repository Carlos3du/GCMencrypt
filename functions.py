
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes as n_random


def encrypt(plaintext: str):
    key = n_random(16)
    cipher = AES.new(key, AES.MODE_GCM) 
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8')) 
    nonce = cipher.nonce
    
    return key, nonce, ciphertext, tag



def decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)  
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)  
        return plaintext.decode('utf-8')
    
    except ValueError:
        return "ERROR: Invalid key"
