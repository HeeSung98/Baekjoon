import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        visited[i] = 1
        Q = deque([i])
        while Q:
            c = Q.popleft()
            for nx in graph[c]:
                if not visited[nx]:
                    visited[nx] = 1
                    Q.append(nx)

print(result)