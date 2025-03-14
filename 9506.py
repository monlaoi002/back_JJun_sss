import math
def find(n):
    divi = set()
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            divi.add(i)
            divi.add(n // i)
    divi.add(1)
    return sorted(list(divi))

def prin(n):
    divi = find(n)
    if sum(divi) == n:
        print(f"{n} = {' + '.join(map(str, divi))}")
    else:
        print(f"{n} is NOT perfect.")

while True:
    a = int(input())
    if a == -1:
        break
    prin(a)