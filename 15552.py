import sys
a = int(input())

for _ in range(a):
    print(sum(map(int,sys.stdin.readline().split())))