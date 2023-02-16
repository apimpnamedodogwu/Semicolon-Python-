universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(list_) -> []:
    enrollment_values = []
    tuition_fees = []
    index = 1

    for data in list_:
        enrollment_values.append(data[1])
        tuition_fees.append(data[2])
        index += 1
    return enrollment_values, tuition_fees


def mean(a_list):
    return sum(a_list) / len(a_list)


def median(a_list):
    a_list.sort()
    count = len(a_list)
    if count % 2 == 0:
        rank = (count // 2)
        med = (a_list[(count // 2) - 1]) + (a_list[rank])
        return med // 2
    else:
        count -= 1
        return a_list[count // 2]


totals = enrollment_stats(universities)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:   {sum(totals[1]):,}")
print(f"Student mean:   {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,.2f}")
print(f"Tuition mean:   {mean(totals[1]):,.2f}")
print(f"Tuition median:   {median(totals[1]):,.2f}")
