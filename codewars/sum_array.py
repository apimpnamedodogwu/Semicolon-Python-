def sum_array(arr):
    if arr is None:
        return 0
    if len(arr) > 1:
        for numbers in arr:
            maximum = max(arr)
            minimum = min(arr)
            result = sum(arr) - (maximum + minimum)
            return result

    elif arr == [] or len(arr) == 1:
        return 0


print(sum_array([]))
