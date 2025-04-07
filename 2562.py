max = 0
indxx = 10
for i in range(9):
    s = int(input())
    if max<s:
        max = s
        indxx = i
        
        
print(max)
print(indxx + 1)