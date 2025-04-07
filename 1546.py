a = int(input())
s = list(map(int,input().split()))

maxx = max(s)
sum = 0

for i in s:
    sum += i / maxx * 100

print(sum/a)