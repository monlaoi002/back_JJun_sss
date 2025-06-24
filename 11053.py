ls = int(input())
ms = list(map(int,input().split()))

d = [1] * ls

for i in range(ls):
    for j in range(i):
        if ms[j] < ms[i]:
            d[i] = max(d[i],d[j] + 1)
            
print(max(d))