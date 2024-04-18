n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
input()
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        if a[i][j] == 1 and lst[i] != lst[j]:
            cnt += 1
print(cnt)
