n, m = map(int, input().split())
a = {i: set() for i in range(n)}
for i in range(m):
    u, v, w = map(int, input().split())
    a[u].add((v, w))
    a[v].add((u, w))
d = [(-1, -1, float("inf"))] * n
for v, w in a[0]:
    d[v] = (0, v, w)
T = {i for i in range(1, n)}
weight = 0
edges = []
for _ in range(n - 1):
    min_w = float("inf")
    j = -1
    for v in T:
        if d[v][2] < min_w:
            min_w = d[v][2]
            j = v
    edges.append(d[j])
    weight += min_w
    T.remove(j)
    for v, w in a[j]:
        if w < d[v][2]:
            d[v] = (j, v, w)
print(weight)
for i in edges:
    print(i[0], i[1])
