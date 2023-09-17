import random
import string

def random_CIN(length: int) -> str:
    result_CIN = ''.join(random.choice(string.digits) for _ in range(length))
    return result_CIN