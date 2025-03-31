s = input()

su = set()
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        su.add(s[i:j])

print(len(su))
