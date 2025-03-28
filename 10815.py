my_cd = int(input())
s1 = set(map(int,input().split()))

my_cd = int(input())
s2 = list(map(int,input().split()))

s_answer = []

for asd in s2:
    if asd in s1:
        s_answer.append(1)
    else:
        s_answer.append(0)
    

print(' '.join(map(str, s_answer)))