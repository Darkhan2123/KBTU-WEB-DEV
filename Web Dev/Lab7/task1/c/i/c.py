import math
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if(math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i))):
        print(i)