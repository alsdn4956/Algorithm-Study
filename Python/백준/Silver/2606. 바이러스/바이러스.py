N = int(input())
C = int(input())

graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

for i in range(C):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(M):
  visited[M] = 1
  for nx in graph[M]:
    if visited[nx] == 0:
      dfs(nx)

dfs(1)
print(sum(visited)-1)