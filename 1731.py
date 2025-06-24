l = int(input())
s = []

for _ in range(l):
    s.append(int(input()))
    
if s[1] - s[0] == s[2] - s[1]:
    d = s[1] - s[0]
    print(s[-1] + d)
else:
    r = s[1] // s[0]
    print(s[-1] * r)