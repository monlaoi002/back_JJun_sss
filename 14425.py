N, M = map(int, input().split())

S = set(input().strip() for _ in range(N)) 

c = sum(1 for _ in range(M) if input().strip() in S)

print(c)
