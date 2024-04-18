def dfs(vertex, G):
    used[vertex] = 1
    for neighbor in G[vertex]:
        if used[neighbor] == 0:
            dfs(neighbor, G)
        elif used[neighbor] == 1:
            stack.append(neighbor)
            print("No")
            exit(0)
    used[vertex] = 2
n, m = map(int, input().split())
G = [[] for i in range(n+1)]
for j in range(m):
    start, finish = map(int, input().split())
    G[start].append(finish)
used = [0] * (n+1)
cycle = []
stack = []
for i in range(n+1):
    if used[i] == 0:
        dfs(i, G)
if len(stack) == 0:
    print("Yes")
