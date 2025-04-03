x,y,w,h = map(int,input().split())
s = []

if x > w - x:
    s.append(w - x)
else:
    s.append(x)

if y > h - y:
    s.append(h - y)
else:
    s.append(y)

print(sorted(s)[0])