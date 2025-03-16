
from functions import encrypt, decrypt
import sys



def main(*args : str):
    text = args[0] if args else "CESAR SCHOOL"
    key, nonce, ciphertext, tag = encrypt(text)
    
    print(f"\nPlain Text: {text}")
    
    print(f"\nKey: {key.hex()}")
    print(f"Nonce: {nonce.hex()}")
    print(f"Tag: {tag.hex()}")
    
    print(f"\nEncrypted Text: {ciphertext.hex()}")

    decrypted_text = decrypt(key, nonce, ciphertext, tag)
    print(f"Decrypted Text: {decrypted_text}\n") 
    
    
if __name__ == "__main__":
    main(*sys.argv[1:])
    
