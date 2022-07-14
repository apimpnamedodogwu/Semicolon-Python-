def love_func(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    if flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    if flower1 % 2 == 0 and flower2 % 2 == 0:
        return False
    if flower1 % 2 != 0 and flower2 % 2 != 0:
        return False
    else:
        return False


print(love_func(1, 4))
