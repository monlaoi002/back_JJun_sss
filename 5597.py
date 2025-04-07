a1 = set()
for _ in range(28):
    a1.add(int(input()))

print('\n'.join(map(str,sorted(list(set(range(1,31))-a1)))))