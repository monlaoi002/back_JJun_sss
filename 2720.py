#q = 25 / d = 10 / n = 5 / p = 1
def j(m,n):#m 받은거 / n 동전
    return m%n,m//n
                
a = int(input())
rjtmfma = [25,10,5,1]
s = []
for _ in range(a):
    s = []
    me = int(input())
    for i in rjtmfma:
        me,e = j(me,i)
        s.append(e)
    print(' '.join(map(str, s)))