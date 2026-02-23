def get_kth(A: list[int], B: list[int], k: int):
    m, n = len(A), len(B)
    total = m + n
    if not (1 <= k <= total):
        return None
    
    def recurse(A, a_base, B, b_base, k):
        if len(A) - a_base > len(B) - b_base:
            A, B = B, A
            a_base, b_base = b_base, a_base

        if a_base >= len(A):
            return B[k - 1]
        elif b_base >= len(B):
            return A[k - 1]
        elif k == 1:
            return min(A[a_base], B[b_base])

        a_add = k // 2
        b_add = k - a_add
        if len(A) < a_base + a_add:
            a_add = len(A) - a_base
            b_add = k - a_add

        if A[a_base + a_add - 1] >= B[b_base + b_add - 1]:
            return recurse(A, a_base, B, b_base + b_add, k - b_add)
        return recurse(A, a_base + a_add, B, b_base, k - a_add)
    
    return recurse(A, 0, B, 0, k)

if __name__ == '__main__':
    A = [1,2,8]
    B = [3,4,5,6,11,13,15,17]
    for k in range(1, len(A) + len(B) + 1):
        print(get_kth(A, B, k))