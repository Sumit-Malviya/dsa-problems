"""
Find wheather the number is armstrong number or not
eg: 153 = 1^3 + 5^3 + 3^3

Constraints:100 ≤ n <1000 
"""


def armstrongNumber(n: int) -> bool:
    # code here
    x = n
    y = n
    digit_count = 0
    arm_num = 0
    if n >= 100 and n < 1000:
        while x > 0:
            x = x // 10
            digit_count += 1
        for i in range(digit_count):
            last_digit = y % 10
            y = y // 10
            arm_num = arm_num + last_digit**digit_count
        if arm_num == n:
            return True
        else:
            return False
