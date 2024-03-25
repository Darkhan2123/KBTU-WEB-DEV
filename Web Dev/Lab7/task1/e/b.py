def power(a, n):
    return a**n

numbers = input().split()

a, b = map(float, numbers)

print(power(a, b))
