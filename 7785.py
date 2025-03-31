c = int(input())

s = set()

for _ in range(c):
    s1,s2 = map(str,input().split())
    if s2 == "enter":
        s.add(s1)
    else:
        s.remove(s1)

print("\n".join(sorted(s, reverse=True)))