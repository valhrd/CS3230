import math
import random

def val(x, y, n):
    return x + n ** y

def radix_sort(arr, d, index):
    m = 3
    for i in range(m):
        digit_grps = [[] for _ in range(d)]
        divisor = d ** i
        for j in range(len(arr)):
            component = arr[j][index]
            digit_grps[(component // divisor) % d].append(arr[j])
        temp = []
        for grp in digit_grps:
            temp.extend(grp)
        arr = temp
    return arr

def sort(arr, n):
    groups = [[] for _ in range(3)]
    for x, y in arr:
        groups[min(2, y - 1)].append((x, y))
    
    for i in range(3):
        groups[i] = radix_sort(groups[i], n, 0)
        if i == 2:
            groups[i] = radix_sort(groups[i], n, 1)
    
    # Merge groups 0 and 1
    temp = []
    i, j = 0, 0
    while i < len(groups[0]) and j < len(groups[1]):
        if val(*groups[0][i], n) <= val(*groups[1][j], n):
            temp.append(groups[0][i])
            i += 1
        else:
            temp.append(groups[1][j])
            j += 1
    temp.extend(groups[0][i:])
    temp.extend(groups[1][j:])
    
    # Merge the intermediary group and group 2
    result = []
    i, j = 0, 0
    while i < len(temp) and j < len(groups[2]):
        if groups[2][j][1] > 3:
            result.append(temp[i])
            i += 1
        else:
            if val(*temp[i], n) <= val(*groups[2][j], n):
                result.append(temp[i])
                i += 1
            else:
                result.append(groups[2][j])
                j += 1
    result.extend(temp[i:])
    result.extend(groups[2][j:])
    return result

def alt_sort(arr, n):
    res = radix_sort(arr, n, 0)
    res = radix_sort(arr, n, 1)
    return res

def verify_sorted(arr, n):
    for i in range(len(arr) - 1):
        if val(*arr[i], n) > val(*arr[i + 1], n):
            return False
    return True

if __name__ == '__main__':
    n = random.randint(10, 31)
    a, b = random.randint(0, n // 2 + 1), random.randint(0, n // 2 + 1)
    arr = [(random.randint(1, n ** 3), 1) for _ in range(a)]
    arr.extend([(random.randint(1, n ** 3), 2) for _ in range(b)])
    arr.extend([(random.randint(1, n ** 3), random.randint(1, n)) for _ in range(n - a - b)])
    random.shuffle(arr)

    print("Before".center(60, '='))
    print(arr)
    print(f"Value of n: {n}")
    print("After".center(60, '='))
    sorted_arr = alt_sort(arr, n)
    print(sorted_arr)
    print(f"Is sorted?: {verify_sorted(sorted_arr, n)}")