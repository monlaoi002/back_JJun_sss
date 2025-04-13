import sys
a = int(sys.stdin.readline())
s = []
for _ in range(a):
    l = int(sys.stdin.readline())
    if l != 0:
        s.append(l)
    else:
        s.pop()

print(sum(s))