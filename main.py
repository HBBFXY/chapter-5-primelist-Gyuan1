def PrimeList(N):
    primes = []
    # 遍历小于N的每个数
    for num in range(2, N):
        is_prime = True
        # 检查是否为质数（只需判断到num的平方根）
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 按要求格式返回结果（空格分隔，末尾无空格）
    return ' '.join(primes)
