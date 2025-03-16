ro = int(input())
for _ in range(ro):
    eogkr = int(input())
    gkreoemf = []
    for i in range(eogkr):
        oor, sul = input().split()
        gkreoemf.append((oor,int(sul)))
    print(max(gkreoemf,key=lambda x: x[1])[0])