a ,b = map(str,input().split())

a1 = int(str(a)[::-1])
b1 = int(str(b)[::-1])

print(max(int(a1),int(b1)))