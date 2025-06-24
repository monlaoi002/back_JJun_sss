l = int(input())
n_cup = 1
for i in range(l):
    s = list(map(int,input().split()))
    if n_cup in s:
        s.remove(n_cup)
        n_cup = s[0]
print(n_cup)