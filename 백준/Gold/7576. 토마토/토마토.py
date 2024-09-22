import sys
from collections import deque

input = sys.stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 상 우 하 좌
M, N = map(int, input().split())

board = []
for n in range(N):
    tmp = (list(map(int, input().split())))
    board.append(tmp)

Q = deque([])

done = 0
total = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            Q.append([n, m])
            done += 1
        if board[n][m] != -1:
            total += 1

result = -1

while Q:
    for _ in range(len(Q)):
        n, m = Q.popleft()
        for dn, dm in direction:
            next_n = n + dn
            next_m = m + dm
            if 0 <= next_n < N and 0 <= next_m < M:
                if board[next_n][next_m] == 0:
                    board[next_n][next_m] = 1
                    done += 1
                    Q.append([next_n, next_m])
    result += 1

if total == done:
    print(result)
else:
    print("-1")