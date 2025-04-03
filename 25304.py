mam = int(input())
a = int(input())

for _ in range(a):
    m ,n = map(int,input().split())
    mam -= m*n
    
if mam == 0:
    print("Yes")
else:
    print("No")