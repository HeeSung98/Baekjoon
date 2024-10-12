import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

def dfs(n, graph, visited):
    visited[n] = 1
    for nx in graph[n]:
        if not visited[nx]:
            dfs(nx, graph, visited)

for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        dfs(i, graph, visited)

print(result)