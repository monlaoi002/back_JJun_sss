def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
a = int(input())
s = list(map(int,input().split()))
s_set = sorted(set(s))
'''
s_set.sort()
s_answer = []

for asd in s:
    s_answer.append(s_set.index(asd))

'''
s_answer = [binary_search(s_set,e)for e in s]

print(' '.join(map(str, s_answer)))