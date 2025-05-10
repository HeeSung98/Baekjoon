import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * m

def backtrack(depth, start):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n + 1):
        arr[depth] = i
        backtrack(depth + 1, i)

backtrack(0, 1)