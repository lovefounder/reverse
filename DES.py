from Crypto.Cipher import DES
import base64


def des_decrypt_ecb(ciphertext, key):
    # Base64解码
    # ciphertext = base64.b64decode(ciphertext_base64)

    # hex ciphertext
    ciphertext = bytes.fromhex(ciphertext)

    # 创建DES对象
    des = DES.new(key, DES.MODE_ECB)

    # 解密数据
    decrypted = des.decrypt(ciphertext)

    return decrypted


# 示例使用
ciphertext = "c4 9d 6f f8 3b 8e 77 8d"
key = b'lovelove'  # DES密钥必须是8字节
decrypted_data = des_decrypt_ecb(ciphertext, key)
print("解密后的数据:", decrypted_data.decode())
