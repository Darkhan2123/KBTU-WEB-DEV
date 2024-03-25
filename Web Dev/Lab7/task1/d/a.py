a = int(input())

array = []

numbers = input().split()
for num in numbers:
    array.append(int(num))

for i in range(0, a, 2):
    print(array[i], end=' ')

print()
