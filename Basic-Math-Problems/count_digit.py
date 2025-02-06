import math

def count_digit(n):
    return int(math.log10(n)) + 1

ans = count_digit(345)
print(ans)
