import math

a = input()
b = len(a)
sum = 0
for i in range(0, b):
    #print(i)
    #print(a[i])
    sum += int(a[b - i - 1]) * 2 ** i
print(sum)