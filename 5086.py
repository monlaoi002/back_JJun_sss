while True:
    u = list(map(int,input().split()))
    
    if u[0] == 0:
        break
    
    if u[1] % u[0] == 0:
        print("factor")
    elif u[0] % u[1] == 0:
        print("multiple")
    else:
        print("neither")