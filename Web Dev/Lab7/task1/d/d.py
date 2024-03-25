a = int(input())

array = []

numbers = input().split()
for num in numbers:
    array.append(int(num))

cnt = 0
reversed_array = array[::-1]

for i in range(a - 1):
    if(reversed_array[i] > reversed_array[i + 1]):
        cnt += 1


print(cnt)