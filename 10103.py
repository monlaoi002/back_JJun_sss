a = int(input())
pyls = [100,100]
for _ in range(a):
    pyls_rol = list(map(int,input().split()))
    if pyls_rol[0]>pyls_rol[1]:
        pyls[1] -= pyls_rol[0]
    if pyls_rol[1]>pyls_rol[0]:
        pyls[0] -= pyls_rol[1]
print(pyls[0])
print(pyls[1])