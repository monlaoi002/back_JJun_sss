import sys

n = int(sys.stdin.readline().strip())

s = []
for _ in range(n):
    s.append(int(sys.stdin.readline().strip()))

s.sort() 
s = set(s)
print("\n".join(map(str,s)))