def points(games):
    count_left = 0

    for a in games:
        left_score = a[0]
        right_score = a[-1]
        if left_score > right_score:
            count_left += 3
        elif left_score == right_score:
            count_left += 1
    return count_left
