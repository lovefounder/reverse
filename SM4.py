from gmssl import sm4


def sm4_decrypt_ecb(ciphertext_hex, key):
    # 将十六进制的密文转换为字节
    ciphertext = bytes.fromhex(ciphertext_hex)

    # 创建SM4对象，使用ECB模式
    sm4_ecb = sm4.CryptSM4()
    sm4_ecb.set_key(key, sm4.SM4_DECRYPT)

    # 解密数据
    decrypted = sm4_ecb.crypt_ecb(ciphertext)

    return decrypted


# 示例使用
ciphertext_hex = "54 7a 18 92 59 d8 5e cf 97 da 91 46 ac da fe c3"  # 替换为你的十六进制编码密文
key = b'lovelovelovelove'  # 替换为你的密钥，必须是16字节

decrypted_data = sm4_decrypt_ecb(ciphertext_hex, key)
print("解密后的数据:", decrypted_data.decode())
