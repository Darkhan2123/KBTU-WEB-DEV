def min_of_four(a, b, c, d):
    return min(a, b, c, d)


numbers = input().split()
a, b, c, d = map(int, numbers)


print(min_of_four(a, b, c, d))
