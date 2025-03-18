n,m = map(int,input().split())
map1 = []
map2 = []
for _ in range(n):
    si = list(map(int,input().split()))
    map1.append(si)
    
for _ in range(n):
    si = list(map(int,input().split()))
    map2.append(si)
    
for i in range(n):
    ss = []
    for j in range(m):
        ss.append(map1[i][j] + map2[i][j])
    print(f"{' '.join(map(str, ss))}")
