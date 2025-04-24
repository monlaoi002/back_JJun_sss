import sys
input = sys.stdin.readline

a,b = map(int,input().split())

s = list(map(int,input().split()))

g = [0] * (a + 1)

for i in range(1,a + 1):
    g[i] = g[i-1] + s[i-1]

for _ in range(b):
    i,j = map(int,input().split())
    print(g[j] - g[i-1])