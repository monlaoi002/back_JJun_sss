import math

def a(N):
    return (math.isqrt(8*N + 1) - 1) // 2

N = int(input())
count = 0
while N > 0:
    a_val = a(N)
    t = a_val*(a_val+1)//2
    N -= t
    count += a_val 

print(count)