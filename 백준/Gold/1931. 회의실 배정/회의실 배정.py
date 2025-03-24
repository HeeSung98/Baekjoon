import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in arr:
    if start >= end_time:  # 이전 회의가 끝난 이후 시작할 수 있다면 배정
        count += 1
        end_time = end

print(count)