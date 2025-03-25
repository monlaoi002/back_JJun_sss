a,b = map(int,input().split())

s = list(map(int,input().split()))

s.sort(reverse=True)

print(s[b-1])