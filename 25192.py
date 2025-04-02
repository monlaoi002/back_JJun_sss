a = int(input())
k = set()
count = 0
for _ in range(a):
    s = input()
    if s == "ENTER":
        count += len(set(k))
        k.clear()
    else:
        k.add(s)
print(count + len(k))