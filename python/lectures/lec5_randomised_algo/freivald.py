import numpy as np

def freivald(
    A: np.array,
    B: np.array,
    C: np.array,
    trials: int = 10,
    v_upper: int = 2,
    logging: bool = False
) -> bool:
    assert A.shape == B.shape == C.shape
    assert trials > 0 and v_upper > 0
    n = A.shape[0]
    assert A.shape == (n, n)


    def freivald_helper():
        v = np.random.randint(0, v_upper, size=(n))
        lhs = np.matmul(A, np.matmul(B, v))
        rhs = np.matmul(C, v)
        return np.all(lhs == rhs)
    
    for _ in range(trials):
        if not freivald_helper():
            if logging:
                print("Certain that: A @ B != C")
            return False
    
    if logging:
        print(f"{(1 - 1 / (v_upper ** trials)) * 100:.5f}% certain that: A @ B == C")
    return True

def standard(
    A: np.array,
    B: np.array,
    C: np.array,
) -> bool:
    return np.all(np.matmul(A, B) == C)

if __name__ == '__main__':
    from tabulate import tabulate
    import time

    # Setup matrices
    n = 1000
    A = np.random.randint(-100, 101, size=(n, n))
    B = np.random.randint(-100, 101, size=(n, n))
    noise_term = np.zeros((n, n))
    noise_term[np.random.randint(n), np.random.randint(n)] = 1
    C = np.matmul(A, B) - noise_term

    start = time.time()
    result = freivald(A, B, C, trials=10)
    freivald_time = time.time() - start
    print(f"Freivald time: {freivald_time}, Equality?: {result}")

    start = time.time()
    result = standard(A, B, C)
    standard_mult_time = time.time() - start
    print(f"Standard comparison time: {standard_mult_time}, Equality?: {result}")
    if freivald_time < standard_mult_time:
        print("Freivald is faster")
    elif freivald_time > standard_mult_time:
        print("Standard comparison is faster")
    else:
        print("Both methods are equally fast")
