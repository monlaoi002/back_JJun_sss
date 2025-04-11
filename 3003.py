ol = [1,1,2,2,2,8]
s = list(map(int,input().split()))

for i in range(len(ol)):
    ol[i] -= s[i]
print(' '.join(map(str,ol)))