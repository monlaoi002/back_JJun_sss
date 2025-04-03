a = int(input())

s = []

for _ in range(a//4):
    s.append("long")
s.append("int")

print(' '.join(s))