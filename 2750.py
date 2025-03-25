a = int(input())
s = []
for _ in range(a):
    s.append(int(input()))

s.sort()

for i in range(a):
    print(s[i])