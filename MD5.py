import hashlib
import itertools
import string

def md5_bruteforce(target_hash, max_length=5):
    chars = string.ascii_lowercase + string.digits  # 定义可以用于暴力破解的字符集
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                return guess
    return None

# 示例使用
target_hash = '99754106633f94d350db34d548d6091a'  # 替换为你的目标哈希值 (例如 "hello" 的 MD5)
found_string = md5_bruteforce(target_hash)
if found_string:
    print("找到匹配的字符串:", found_string)
else:
    print("未找到匹配的字符串。")
