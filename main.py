import math

def PrimeList(N):
    primes = []
    # 遍历2到N-1的所有数字
    for num in range(2, N):
        is_prime = True
        # 检查是否能被2到sqrt(num)整除
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 转换为空格分隔的字符串
    return ' '.join(primes)
