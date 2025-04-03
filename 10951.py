import sys

while True:
    l = list(map(int,sys.stdin.readline().split()))
    if l:
        print(sum(l))
    else:
        break