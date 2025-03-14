v = int(input())
s = input()

if v == 1:
    print(s)
else:
    count_a = s.count('A')
    count_b = s.count('B')
    
    if count_a > count_b:
        print("A")
    elif count_a < count_b:
        print("B")
    else:
        print("Tie")
