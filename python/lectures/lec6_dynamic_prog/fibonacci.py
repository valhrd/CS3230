# Time Complexity: O(n)
# Space Complexity: O(1)
def fibonacci_iter(n: int) -> int:
    assert n >= 0
    if n <= 1:
        return n
    
    a, b = 1, 0
    while n > 1:
        a, b = a + b, a
        n -= 1
    return a

h = {}
def fibonacci_recur(n: int) -> int:
    if n <= 1:
        return n
    if n in h:
        return h[n]
    t = fibonacci_iter(n - 1) + fibonacci_iter(n - 2)
    h[n] = t
    return t

if __name__ == '__main__':
    for i in range(100):
        print(fibonacci_recur(i))