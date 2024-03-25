a = int(input())
i = 0

flag = True

while(flag):
    if(2 ** i >= a):
        flag = False
        print(i)
    i += 1
