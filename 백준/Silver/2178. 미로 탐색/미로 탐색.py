import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
visited = [[0 for _ in range(M)]for _ in range(N)]
visited[0][0] = 1

for i in range(N):
    board.append(list(map(int, input().strip())))

Q = deque([])
Q.append((0, 0))

while Q:
    x, y = Q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] += visited[x][y] + 1
                Q.append((nx, ny))

print(visited[N - 1][M - 1])