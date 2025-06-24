while True:
    s = input()
    if s == '0':
        break
    numa = [int(ch) for ch in s]
    

    while numa:
        if numa[0] == numa[-1]:
            numa = numa[1:-1]
        else:
            print("no")
            break
    else:
        print("yes")
