import sys
from collections import deque

input = sys.stdin.readline

n, v, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs_result = []
bfs_result = []

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v] = 1
    dfs_result.append(v)
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(s)

Q = deque([s])
visited = [0] * (n + 1)

visited[s] = 1
while Q:
    v = Q.popleft()
    bfs_result.append(v)
    for nx in graph[v]:
        if visited[nx] == 0:
            visited[nx] = 1
            Q.append(nx)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))