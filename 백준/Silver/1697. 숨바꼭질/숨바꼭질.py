import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)

def bfs(n, m):
    Q = deque()
    Q.append(n)
    
    while Q:
        now = Q.popleft()
        if now == m:
            return visited[now]
        for i in (now - 1, now + 1, now * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[now] + 1
                Q.append(i)

result = bfs(n, m)
print(result)