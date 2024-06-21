from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def aes_decrypt(ciphertext, key):
    # Decode the base64 encoded ciphertext
    # ciphertext = base64.b64decode(ciphertext)

    # hex ciphertext
    ciphertext = bytes.fromhex(ciphertext)

    # Create the cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the ciphertext
    decrypted = cipher.decrypt(ciphertext)

    return decrypted


ciphertext = "81 49 2a db b4 c4 0e e9 26 3c aa b1 3d 21 2e d8"
key = b'lovelovelovelove'  # 密钥字节必须为 16, 24, 或 32

decrypted_message = aes_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message.decode())
