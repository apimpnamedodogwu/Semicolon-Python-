def convert_cel_to_far(temp) -> float:
    temp_in_far = temp * 9 / 5 + 32
    return round(temp_in_far, 2)


print(convert_cel_to_far(60))


def convert_far_to_cel(temp) -> float:
    temp_in_cel = (temp - 32) * 5 / 9
    return round(temp_in_cel, 2)


print(convert_far_to_cel(60))
