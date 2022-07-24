import math


def century(years) -> int:
    if years % 100 == 0:
        return years // 100
    else:
        return math.ceil(years / 100)


print(century(89))
