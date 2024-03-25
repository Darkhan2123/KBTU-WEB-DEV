def xor(a, b):
    return a ^ b

numbers = input().split()
a, b = map(int, numbers)

print(xor(a, b))