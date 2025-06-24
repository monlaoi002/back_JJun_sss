import sys

n_len, t_len = map(int, sys.stdin.readline().split())

s = list(map(int, sys.stdin.readline().split()))

s[:t_len] = sorted(s[:t_len])

print(" ".join(map(str, s)))
