a = int(input())
k = []
for _ in range(a):
    k.append(int(input()))
count_0 = k.count(0)
count_1 = k.count(1)

if count_0 > count_1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")