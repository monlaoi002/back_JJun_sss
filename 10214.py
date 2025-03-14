a = int(input())
for _ in range(a):
    Y = G = 0
    
    for _ in range(9):
        y, g = map(int, input().split())
        Y += y
        G += g
    
    if Y > G:
        print('Yonsei')
    elif Y < G:
        print('Korea')
    else:
        print("Draw")