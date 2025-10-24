def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    for num in range(2, N):
        # 质数判断：从2到num-1检查是否能整除
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)
