# 기본상태에서 최외각 사각형 한 변 위에있는 점의 계수
# n번 이동시) 이전 점의 계수  * 2 - 1
# n>=1

a = int(input())
st = 2
for i in range(1,a+1):
    st = st*2 - 1
print(st**2)