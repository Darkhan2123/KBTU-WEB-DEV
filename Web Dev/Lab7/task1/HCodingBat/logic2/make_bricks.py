def make_bricks(small, big, goal):
    # Calculate the total length of bricks we have (big bricks + small bricks)
    total_length = big * 5 + small

    # Check if the total length is greater than or equal to the goal
    if total_length >= goal:
        # Check if we have enough small bricks to reach the goal,
        # or if we can use some big bricks and the remaining small bricks to reach the goal
        return small >= goal % 5 or (goal - big * 5) <= small
    else:
        return False
