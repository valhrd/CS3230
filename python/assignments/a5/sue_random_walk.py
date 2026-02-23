import numpy as np

N = 4
adjacent_points = [
    [(i - 1) % N, (i + 1) % N] for i in range(N)
]

paths = np.array([0] * N)
def run():
    pos = 0
    s = {pos}
    while len(s) != N:
        d = np.random.randint(0,2)
        pos = adjacent_points[pos][d]
        s.add(pos)
    paths[pos] += 1

for _ in range(100000):
    run()
print(paths / np.sum(paths))
