import hashlib
import itertools
import string

def sha256_bruteforce(target_hash, max_length=5):
    chars = string.ascii_lowercase + string.digits  # 可以扩展到所有可能的字符集
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                return guess
    return None

# 示例使用
target_hash = '6ac3c336e4094835293a3fed8a4b5fedde1b5e2626d9838fed50693bba00af0e'  # 替换为你的目标哈希值
found_string = sha256_bruteforce(target_hash)
if found_string:
    print("找到匹配的字符串:", found_string)
else:
    print("未找到匹配的字符串。")
