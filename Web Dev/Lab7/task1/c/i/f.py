a = input()
a = a[::-1]
b = len(a)

flag = False
#100
#001
for i in range(b):
    if not flag and a[i] == '0':
        continue
    else:
        flag = True
        print(a[i], end='')