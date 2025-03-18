maap = []
for _ in range(9):
    s = list(map(int,input().split()))
    maap.append(s)

maxv = max(max(row) for row in maap)
for i, row in enumerate(maap):
    for j, value in enumerate(row):
        if value == maxv:
            print(maxv)
            print(i+1,j+1)