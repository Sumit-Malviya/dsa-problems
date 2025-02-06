"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints: -231 <= x <= 231 - 1
"""


def isPalindrome(x: int) -> bool:
    n = x
    reversed = 0
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        while n > 0:
            last_digit = n % 10
            reversed = reversed * 10 + last_digit
            n = n // 10
            if reversed == x:
                if x in range(1, 2**31):
                    return True
                else:
                    return False
            else:
                return False
