x = int(input())
y = int(input())
a = 0
if x > 0:
    if y > 0:
        a = 1
    else:
        a = 4
else:
    if y > 0:
        a = 2
    else:
        a = 3

print(a)