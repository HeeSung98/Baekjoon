import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []

for _ in range(T):
    M, N, K = map(int, input().split())

    board = [[0 for _ in range(M)] for _ in range(N)] 
    check = [[0 for _ in range(M)] for _ in range(N)]


    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    count = 0

    for n in range(N):
        for m in range(M):
            if board[n][m] == 1 and check[n][m] == 0:
                count += 1
                Q = deque([])
                Q.append([m, n])
                check[n][m] = 1
                while Q:
                    for _ in range(len(Q)):
                        x, y = Q.popleft()
                        flag = True
                        for dx, dy in direction:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < M and 0 <= ny < N:
                                if board[ny][nx] == 1 and check[ny][nx] == 0:
                                    check[ny][nx] = 1
                                    Q.append([nx, ny])
    

    result.append(count)

for i in result:
    print(i)