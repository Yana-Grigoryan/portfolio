import random
import math
from matplotlib import pyplot

#  интеграл x^2dx om 1 до 2 = 7/3

N = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
t = []
k = []
for n in N:
    for j in range(0, 100):
        s = []
        for i in range(0, n):
            r = random.random()
            x = 1 + r
            s.append(x)

        s = [k ** 2 for k in s]
        m = sum(s)
        i = (abs(7/3 - m/n)) / (7/3)
        t.append(i)
    delta = sum(t) / len(t)
    k.append(delta)
for l in range(0, len(k)):
    print(f'Delta{l} = ', k[l])


def listlog(c):
    for i in range(0, len(c)):
        c[i] = math.log(c[i])
    return c


k = listlog(k)
N = listlog(N)
pyplot.scatter(N, k)
pyplot.plot([N[0],N[9]], [k[0],k[9]], color='red')
pyplot.plot([N[1],N[8]], [k[1],k[8]], color='blue')
pyplot.show()


