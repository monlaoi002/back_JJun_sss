def fabo(ls,n):
    ls.append(ls[-1] + ls[-2])
    if n == 0:
        return ls
    return fabo(ls,n - 1)

a = int(input())
lss = [0,1]

if a == 0:
    print(lss[0])
elif a == 1:
    print(lss[1])
else:
    print(fabo(lss,a)[-3])