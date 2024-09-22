import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

board = []
for h in range(H):
    tmp = []
    for n in range(N):
        tmp.append(list(map(int, input().split())))
    board.append(tmp)

direction = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


Q = deque([])
done, total, result = 0, 0, -1 # 익은 토마토, 전체 토마토, 출력할 결과

for h in range(H):
    for n in range(N):
        for m in range(M):
            if board[h][n][m] == 1:
                Q.append([h, n, m])
                done += 1
            if board[h][n][m] != -1:
                total += 1

while Q:
    for _ in range(len(Q)):
        h, n, m = Q.popleft()
        for dh, dn, dm in direction: # dh -> direction h
            nh, nn, nm = h + dh, n + dn, m + dm # nh -> next n
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if board[nh][nn][nm] == 0:
                    board[nh][nn][nm] = 1
                    Q.append([nh, nn, nm])
                    done +=1
    result += 1

if done == total:
    print(result)
else:
    print("-1")