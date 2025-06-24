import sys
n = int(sys.stdin.readline())
sas = list(map(int, sys.stdin.readline().split()))

counter = 0

for i in range(n - 1):
    if sas[i] > sas[i+1]:

        newv = sas[i+1]
        countsft = 0
        
        while sas[i] > newv:
            newv *= 2
            countsft += 1
            if newv == 0:
                break

        sas[i+1] = newv
        counter += countsft

print(counter)
