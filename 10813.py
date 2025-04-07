n ,m = map(int,input().split())

s = list(range(n+1))

for _ in range(m):
    l1,l2 = map(int,input().split())
    bb = s[l1]
    s[l1] = s[l2]
    s[l2] = bb
print(' '.join(map(str,s[1:n+1])))   