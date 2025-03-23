a = int(input())
countt = 0
while a > 0 and a % 5 != 0:
    a -= 3
    countt += 1

if a < 0:
    print(-1)
else:
    print(countt + a // 5)
