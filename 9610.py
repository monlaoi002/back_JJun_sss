a = int(input())
Q1,Q2,Q3,Q4,AXIS = 0,0,0,0,0
for _ in range(a):
    ars = list(map(int,input().split()))
    if ars[0] == 0 or ars[1] == 0:
        AXIS += 1
    elif ars[0] * ars[1] > 0:
        if ars[0] > 0:
            Q1 += 1
        else:
            Q3 += 1
    else:
        if ars[0] > 0:
            Q4 += 1
        else:
            Q2 += 1
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)