a = int(input())

array = []

numbers = input().split()
for num in numbers:
    array.append(int(num))

for i in range(a):
    if(array[i] % 2 == 0):
        print(array[i], end=' ')

print()