import sys
from collections import deque

input = sys.stdin.readline

# 입력값 처리
N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

# 초기화
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * N for _ in range(N)]
result = []

def bfs(x, y):
    Q = deque([(x, y)])
    visited[x][y] = True
    size = 1  # 단지 크기 카운트
    
    while Q:
        cx, cy = Q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append((nx, ny))
                size += 1
    return size

# 단지 탐색
for x in range(N):
    for y in range(N):
        if board[x][y] and not visited[x][y]:
            result.append(bfs(x, y))

# 출력
result.sort()  # 단지 크기 정렬
print(len(result))  # 단지 수 출력
for r in result:
    print(r)  # 각 단지 크기 출력
