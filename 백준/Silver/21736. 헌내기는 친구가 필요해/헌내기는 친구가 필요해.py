import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

Q = deque([])
for i in range(n):
    tmp = input().strip()
    if 'I' in tmp:
        Q.append([i, tmp.find('I')])
    board.append(tmp)

result = 0
while Q:
    cx, cy = Q.popleft()
    if visited[cx][cy] == 0:
        visited[cx][cy] = 1
    for dx, dy in direction:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'X':
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if board[nx][ny] == 'P':
                    result += 1
                Q.append([nx, ny])

if result:
    print(result)
else:
    print("TT")