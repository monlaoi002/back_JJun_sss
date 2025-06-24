moum = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input().lower()
    if s == '#':
        break
    count = 0
    for i in moum:
        count += s.count(i)
    print(count)