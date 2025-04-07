n,m = map(int,input().split())

s = [0]*101

for f in range(m):
    i,j,k = map(int,input().split())
    i -= 1
    s[i:j] = [k] * (j-i)
    
print(' '.join(map(str,s[:n])))