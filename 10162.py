a = int(input())
index = 0
sec = [5 * 60,60,10]
buttons = [0 ,0 ,0]
if a % sec[2] != 0:
    print(-1)
else:
    while a>0 and index < len(sec):
        if a>=sec[index]:
            a -= sec[index]
            buttons[index] += 1
        else:
            index += 1
    print(' '.join(map(str, buttons)))