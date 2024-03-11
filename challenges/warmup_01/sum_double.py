# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
    return (a + b) * 2 if a == b else a + b


if __name__ == '__main__':
    print(sum_double(1, 2))
    print(sum_double(3, 2))
    print(sum_double(2, 2))
