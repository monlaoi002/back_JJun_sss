l = input()
a = len(l)
ran = a // 2 + 1 if a % 2 != 0 else a // 2
for i in range(ran):
    if l[i] != l[a-i-1]:
        print(0)
        break
else:
    print(1)