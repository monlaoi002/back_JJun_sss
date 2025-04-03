# 세 꼭짓점의 좌표 입력 받기
xs = []
ys = []

for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xd = [x for x in xs if xs.count(x) == 1][0]
yd = [y for y in ys if ys.count(y) == 1][0]

print(xd, yd)
