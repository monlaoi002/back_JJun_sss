a = int(input())
for _ in range(a):
    scorrr = 0
    gajung = 0
    s = input()
    
    for i in s:
        if i == "O":
            gajung += 1
            scorrr += gajung
        else:
            gajung = 0
            
    print(scorrr)
    