n = int(input())
a_s = set(map(int,input().split()))
mm = int(input())

m = list(map(int,input().split()))

answer = []

for i in m:
    k = 0
    if i in a_s:
        k = 1
    answer.append(k)
    
print("\n".join(map(str,answer)))