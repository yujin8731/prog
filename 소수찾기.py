def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    cnt = 0
    for i in range(1,n + 1):
        if isprime(i):
            cnt += 1
    return cnt