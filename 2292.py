a = int(input())
n = 2
if a == 1:
    print(a)
else:
    while True:
        a -= 6*(n-1)
        if a <= 1:
            break
        n += 1
    print(n)