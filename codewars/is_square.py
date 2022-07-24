import math


# This method does not count 0 as a square!
def is_square(number):
    for num in range(1, number, 1):
        if num ** 2 == number:
            return True
    else:
        return False


print(is_square(0))


def is_square_two(number) -> int:
    if number < 0:
        return False
    square = int(math.sqrt(number))
    return True if (square ** 2) == number else False


print(is_square_two(-1))
