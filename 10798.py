a = []
s = ""

for _ in range(5):
    a.append(input())
    
maxl = max(len(w) for w in a)

for i in range(maxl):
    for j in range(5):
        if i < len(a[j]):
            s += a[j][i]

print(s)