h = list(map(int,input().split()))
if h[1] < 45:
    h[0] -= 1
    h[1] += 60
if h[0] < 0:
    h[0] = 23
h[1] -= 45

print(h[0],h[1])