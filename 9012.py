a = int(input())
for _ in range(a):
    s = input().strip()
    smm = []  
    err = False

    if s.count('(') != s.count(')') or s[0] == ')' or s[-1] == '(':
        print("NO")
        continue

    # 스택 기반 처리
    for char in s:
        if char == '(':
            smm.append('(')
        else:
            if smm and smm[-1] == '(':
                smm.pop()
            else:
                err = True
                break

    print("YES" if not err and not smm else "NO")
