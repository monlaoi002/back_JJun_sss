i = input()
base = i[0]
h = 10

for a in range(1,len(i)):
    if base == i[a]:
        h += 5
    else:
        h += 10
        base = i[a]
        
print(h)