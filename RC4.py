from Crypto.Cipher import ARC4
import base64


def rc4_decrypt(ciphertext, key):
    # Base64解码密文
    # ciphertext = base64.b64decode(ciphertext)

    # hex ciphertext
    ciphertext = bytes.fromhex(ciphertext)

    # 创建RC4对象
    rc4 = ARC4.new(key)

    # 解密数据
    decrypted = rc4.decrypt(ciphertext)

    return decrypted


# 示例使用
ciphertext = "86 16 c2 2d" 
key = b'love'  # 替换为你的密钥

decrypted_data = rc4_decrypt(ciphertext, key)
print("解密后的数据:", decrypted_data.decode())
