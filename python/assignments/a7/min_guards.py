def min_guards(guards: list[list], M: int) -> list[list]:
    guards.sort()
    uncovered = 1
    p = 0
    res = []
    while uncovered <= M:
        guard = None
        best_end = -float('inf')
        while p < len(guards) and guards[p][0] <= uncovered:
            if guards[p][1] > best_end:
                best_end = guards[p][1]
                guard = guards[p]
            p += 1
        
        if guard is not None:
            res.append(guard)
            uncovered = best_end + 1
    return res

def check_valid_input(guards: list[int], M: int) -> bool:
    guards = sorted(guards)
    temp = []
    for g in guards:
        a, b = g
        if not temp:
            temp.append([a, b])
        else:
            if temp[-1][1] + 1 >= g[0]:
                temp[-1][1] = max(temp[-1][1], g[1])
            else:
                return False
    return temp[0] == [1, M]

def gen_guards(n: int, M: int) -> list[int]:
    guards = [list(sorted([random.randint(2, M - 1), random.randint(2, M - 1)])) for _ in range(n)]
    guards.append([1, random.randint(1, M // 2)])
    guards.append([random.randint(M // 2, M), M])
    return guards

if __name__ == '__main__':
    import random
    n = 40
    M = 100
    
    guards = gen_guards(n, M)
    while not check_valid_input(guards, M):
        guards = gen_guards(n, M)

    print(guards)
    print(min_guards(guards, M))