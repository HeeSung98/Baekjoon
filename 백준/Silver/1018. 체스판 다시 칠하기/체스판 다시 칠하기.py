n, m = map(int, input().split())
board = []
result = 9999

for i in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if(a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if board[a][b] != 'B':
                        draw2 += 1
                    else:
                        draw1 += 1
        result = min(result, draw1, draw2)

print(result)