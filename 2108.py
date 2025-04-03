#pypy3 환경

import sys

def sec(lst):
    f = {}
    
    for n in lst:
        if n in f:
            f[n] += 1
        else:
            f[n] = 1
    mxc = max(f.values())
    
    mod = []
    for k in f:
        if f[k] == mxc:
            mod.append(k)
    
    mod.sort()
    if len(mod) > 1:
        return mod[1]
    else:
        return mod[0]

a = int(input())
s = []
for _ in range(a):
    s.append(int(input()))

m1 = sum(s)
print(round(m1/a))

s.sort()
print(s[a//2])

print(sec(s))

print(max(s)-min(s))
