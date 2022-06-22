# def is_prime(num: int) -> bool:
#     max_divisor = (num // 2) + 1
#     for number in range(2, max_divisor):
#         if num % number == 0:
#             return False
#         return True
#
#
# print(is_prime(67))


def is_prime_two(num: int) -> bool:
    factor_of_number, count = 0, 1
    while count <= num:
        if num % count == 0:
            factor_of_number += 1
        count += 1

    if factor_of_number == 2:
        return True
    return False


# print(is_prime_two(67))

prime = [i for i in range(1, 10) if is_prime_two(i)]
print(prime)
