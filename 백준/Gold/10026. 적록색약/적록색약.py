import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 상 우 하 좌
board1 = []
board2 = []

for i in range(n):
    row = input().strip()
    board1.append(row)
    board2.append(row.replace('R', 'Y').replace('G', 'Y'))

Q = deque([])
result1 = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            Q.append([i, j])
            visited[i][j] = 1
            result1 += 1
            while Q:
                cx, cy = Q.popleft()
                now = board1[cx][cy]
                for dx, dy in direction:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board1[nx][ny] == now:
                        Q.append([nx, ny])
                        visited[nx][ny] = 1

Q = deque([])
result2 = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            Q.append([i, j])
            visited[i][j] = 1
            result2 += 1
            while Q:
                cx, cy = Q.popleft()
                now = board2[cx][cy]
                for dx, dy in direction:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board2[nx][ny] == now:
                        Q.append([nx, ny])
                        visited[nx][ny] = 1
                        

print(result1, result2)