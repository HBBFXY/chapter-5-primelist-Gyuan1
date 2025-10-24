def PrimeList(N):
    # 处理N小于2的情况
    if N <= 2:
        return ""
    prime_list = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        is_prime = True
        # 检查是否为质数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(str(num))
    # 转换为空格分隔的字符串
    return " ".join(prime_list)
