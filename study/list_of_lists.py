def enrollment_stats(university_list):
    enrolled_students = []
    annual_fees = []

    for university in university_list:
        enrolled_students.append(university[1])
        annual_fees.append(university[2])

    return enrolled_students, annual_fees


def mean(a_list):
    return sum(a_list) / len(a_list)


def median(a_list):
    a_list.sort()
    if len(a_list) % 2 == 0:
        left_center = (len(a_list) - 1 // 2)
        right_center = (len(a_list) + 1 // 2)
        return [a_list[left_center], a_list[right_center]]
    else:
        var = len(a_list) % 2 == 1
        middle = int(len(a_list) / 2)
        return a_list[middle]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

total = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(total[0]):,}")
print(f"Total tuition:  $ {sum(total[1]):,}")
print(f"\nStudent mean:     {mean(total[0]):,.2f}")
print(f"Student median:   {median(total[0]):,}")
print(f"\nTuition mean:   $ {mean(total[1]):,.2f}")
print(f"Tuition median: $ {median(total[1]):,}")
print("*****" * 6)
print("\n")
