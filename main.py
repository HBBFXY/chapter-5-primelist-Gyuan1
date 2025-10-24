import math

def PrimeList(N):
    # 处理N≤2的情况
    if N <= 2:
        return ""
    primes = []
    for num in range(2, N):
        is_prime = True
        # 优化：2是唯一偶质数，先判断偶数
        if num % 2 == 0 and num != 2:
            continue
        # 只检查奇数除数
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return ' '.join(primes)
