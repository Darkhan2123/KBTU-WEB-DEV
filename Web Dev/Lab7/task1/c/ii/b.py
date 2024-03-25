a = int(input())

i = 2
flag = True

while(flag):
    if(a % i == 0):
        print (i)
        flag = False
    i += 1