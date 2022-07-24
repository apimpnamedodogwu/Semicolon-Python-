def double_char(s):
    new_ = ""
    for letter in s:
        new_ += letter * 2

    return new_


print(double_char("String"))


def double_char(s):
    newer = []
    for letter in s:
        newer.append(letter * 2)
    return ''.join(newer)


print(double_char("String"))
