# With path compression
def root(x: int, ids: list[int]) -> int:
    nodes = [x]
    while x != ids[x]:
        x = ids[x]
        nodes.append(x)
    for node in nodes:
        ids[node] = x
    return x

def union(p: int, q: int, ids: list[int], size: list[int]):
    a, b = root(p, ids), root(q, ids)
    if a == b:
        return
    
    if size[a] < size[b]:
        ids[b] = a
        size[a] += size[b]
    else:
        ids[a] = b
        size[b] += size[a]

def find(p: int, q: int, ids: list[int]) -> bool:
    return root(p, ids) == root(q, ids)

if __name__ == '__main__':
    N = 7
    ids = [i for i in range(N)]
    size = [1 for _ in range(N)]

    union(2, 4, ids, size)
    find(2, 3, ids)
    union(3, 6, ids, size)
    union(2, 6, ids, size)

    print(ids)