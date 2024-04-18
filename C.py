n, m = map(int, input().split())
a = []
boom = [i for i in range(n)]
temp = m
for f in range(m):
    cnt = 0
    u, v = map(int, input().split())
    if boom[u] != boom[v]:
        j = boom[v]
        for i in range(n):
            if boom[i] == j:
                boom[i] = boom[u]
    for i in range(1, n):
        if boom[i] != boom[i - 1]:
            cnt += 1
            break
    if cnt == 0:
        temp = f + 1
        break
print(temp)
