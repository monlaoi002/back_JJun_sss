n = int(input())

for _ in range(n):
    num = list(map(int,input().split()))
    if num[1] - num[2] > num[0]:
        print("advertise")
    elif num[1] - num[2] == num[0]:
        print("does not matter")
    else:
        print("do not advertise")