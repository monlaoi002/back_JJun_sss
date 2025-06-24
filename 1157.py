s = input().upper()

dic = {}

for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
m_s = max(dic.values())

kkk = [k for k, v in dic.items() if v == m_s]

if len(kkk) == 1:
    print(kkk[0])
else:
    print("?")