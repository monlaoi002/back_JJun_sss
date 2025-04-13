import sys

a = int(sys.stdin.readline())
stk = []
s = []

for _ in range(a):
    asd = list(map(int,sys.stdin.readline().split()))
    
    if asd[0] == 1:
        stk.append(asd[1])
    elif asd[0] == 2:
        if not stk:
            s.append(-1)
        else:
            s.append(stk[-1])
            stk.pop()
    elif asd[0] == 3:
        s.append(len(stk))
    elif asd[0] == 4:
        if not stk:
            s.append(1)
        else:
            s.append(0)
    elif asd[0] == 5:
        if not stk:
            s.append(-1)
        else:
            s.append(stk[-1])
            
print('\n'.join(map(str,s)))
        