j = int(input())
arrays = []  # 모든 배열을 저장할 리스트

for _ in range(j):
    numbers = list(map(int, input().split()))
    numbers.sort()
    if numbers[0] == numbers[1] == numbers[2]:
        arrays.append(numbers[0] * 1000 + 10000)
    elif numbers[0] == numbers[1] or numbers[2] == numbers[1]:
        arrays.append(numbers[1] * 100 + 1000)
    else:
        arrays.append(numbers[2]*100)
arrays.sort()
print(arrays[j-1])