a = int(input())

array = []

numbers = input().split()
for num in numbers:
    array.append(int(num))


cnt = 0
for i in range(a):
    if(array[i] > 0):
        cnt+= 1

print(cnt)