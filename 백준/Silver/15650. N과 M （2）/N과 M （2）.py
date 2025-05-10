import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * m  # 결과를 담을 배열

def backtrack(depth, start):
    if depth == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n + 1):
        arr[depth] = i
        backtrack(depth + 1, i + 1)

backtrack(0, 1)