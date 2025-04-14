def aaaa(n,a = 1):
    if n == 0:
        return a
    else:
        return aaaa(n - 1,a * n)
        
s = int(input())

if s == 0:
    print(1)
else:
    print(aaaa(s))