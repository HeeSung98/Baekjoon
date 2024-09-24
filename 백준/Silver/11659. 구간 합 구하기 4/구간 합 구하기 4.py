import sys

input = sys.stdin.readline

result = []

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [0] * (len(arr) + 1)

for i in range(1, len(arr) + 1):
    tmp[i] = arr[i - 1] + tmp[i - 1]

for _ in range(m):
    start, end = map(int, input().split())
    result.append(tmp[end] - tmp[start - 1])

for i in result:
    print(i)