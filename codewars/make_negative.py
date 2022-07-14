def make_negative(number):
    if number < 0:
        return number
    else:
        num = "-" + str(number)
        return int(num)
