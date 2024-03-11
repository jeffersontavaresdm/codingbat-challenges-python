# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n
# is over 21.
#
# diff21(10) → 11
# diff21(21) → 0
# diff21(50) → 58

def diff21(n):
    return (21 - n if n <= 21 else n - 21) * 2 if n > 21 else 21 - n


if __name__ == '__main__':
    print(diff21(10))
    print(diff21(21))
    print(diff21(50))
