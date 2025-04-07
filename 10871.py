leng , t = map(int,input().split())

s = list(map(int,input().split()))
li = []
for i in s:
    if t>i:
        li.append(i)

print(' '.join(map(str, li)))