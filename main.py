def PrimeList(N):
    primes = []
    # 遍历小于N的每个数
    for num in range(2, N):
        is_prime = True
        # 检查是否为质数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 按要求格式输出（空格分隔，末尾无空格）
    return ' '.join(primes)

# 示例测试（可根据需要删除）
print(PrimeList(10))  # 输出: 2 3 5 7
