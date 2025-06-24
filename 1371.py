import sys
f = {}
s = sys.stdin.read().replace('\n','')

for i in s:
    if i != ' ':
        f[i] = f.get(i,0) + 1

maxV = max(f.values())
maxK = [k for k, v in f.items() if v == maxV]
maxK.sort()

print(''.join(map(str,maxK)))


