import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
visitied = [[0 for _ in range(M)] for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(N):
    board.append(list(map(int, input().split())))

    
def bfs():
    while Q:
        x, y, distance = Q.popleft()
        if not visitied[x][y]:
            visitied[x][y] = distance + 1
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if 0 <= cx < N and 0 <= cy < M and not visitied[cx][cy] and board[cx][cy]:
                    distance = visitied[x][y]
                    Q.append((cx, cy, distance))
    return

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            Q = deque([])
            Q.append((i, j, -1))
            bfs()
            visitied[i][j] = 0

for i in range(N):
    for j in range(M):
        if not visitied[i][j] and board[i][j] == 1:
            visitied[i][j] = -1
    print(*visitied[i])