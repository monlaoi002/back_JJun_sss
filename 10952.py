import sys

while True:
    x = sum(map(int,sys.stdin.readline().split()))
    if x == 0:
        break
    print(x)
    