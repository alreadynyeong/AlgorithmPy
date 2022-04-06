n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(g, s, v):
    v[s] = 1
    for i in g[s]:
        if not v[i]:
            dfs(g, i, v)

dfs(graph, 1, visited)
print(sum(visited)-1)