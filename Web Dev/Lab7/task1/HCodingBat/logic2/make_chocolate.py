def make_chocolate(small, big, goal):
    max_big_kilos = big * 5

    remaining_kilos = goal - min(goal // 5, big) * 5

    if remaining_kilos <= small:
        return remaining_kilos
    else:
        return -1