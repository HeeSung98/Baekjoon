import sys
from collections import deque

input = sys.stdin.readline

board = [0] * 101
visited = [False] * 101
sadari, baem = map(int, input().split())

for _ in range(sadari):
    a, b = map(int, input().split())
    board[a] = b

for _ in range(baem):
    a, b = map(int, input().split())
    board[a] = b

Q = deque([[1, 0]])

visited[1] = True
while Q:
    now, count = Q.popleft()
    visited[now] = 1

    if now == 100:
        print(count)
        break

    for i in range(1, 7):
        next = now + i
        if next <= 100:
            if board[next] != 0:
                next = board[next]
            if not visited[next]:
                visited[next] = True
                Q.append([next, count + 1])
