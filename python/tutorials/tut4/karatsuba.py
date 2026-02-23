def karatsuba(a: int, b: int) -> int:
    n = bits(a)
    if n <= 1:
        return a * b
    
    half = n // 2
    a_left, a_right = a >> (half), a % (1 << half)
    b_left, b_right = b >> (half), b % (1 << half)

    x = karatsuba(a_left, b_left)
    z = karatsuba(a_right, b_right)
    y = karatsuba(a_left + a_right, b_left + b_right) - x - z

    return (x << (2 * half)) + (y << (half)) + z

def bits(n: int) -> int:
    res = 0
    while n > 0:
        n >>= 1
        res += 1
    return res

if __name__ == '__main__':
    import random
    import time

    def gen_nums(n_bits):
        A = random.randint(1 << n_bits, 1 << (n_bits + 1))
        B = random.randint(1 << n_bits, 1 << (n_bits + 1))
        return A, B
    
    total_time = []
    for n in range(1000, 1050):
        A, B = gen_nums(n)
        
        start = time.time()
        res = karatsuba(A, B)
        karatsuba_time = time.time() - start

        start = time.time()
        res = A * B
        standard_mult_time = time.time() - start

        total_time.append((karatsuba_time, standard_mult_time))

    for p in total_time:
        print(p)