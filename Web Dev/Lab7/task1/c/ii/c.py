a = int(input())

i = 0
flag = True

while(flag):
    if(2 ** i > a):
        flag = False
        break
    print(2 ** i)
    i += 1