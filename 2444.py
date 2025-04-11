a = int(input())

for i in range(a * 2 - 1):
    print(" " * abs(a - i -1) + "*" * (2*(a - abs(a - i -1)) -1))