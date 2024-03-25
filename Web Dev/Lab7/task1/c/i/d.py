a = int(input())
b = int(input())
cnt = 0

a = str(a)

for i in a:
    if(int(i) == b):
        cnt+= 1
print(cnt)