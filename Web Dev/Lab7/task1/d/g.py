N = int(input())
array = list(map(int, input().split()))

array = array[::-1]

for i in range(0, N):
    print(array[i], end=' ')