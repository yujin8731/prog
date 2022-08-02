def solution(n):
    a = str(n)
    print(a)
    b = list(a)
    print(b)
    c = list(map(int, b))
    print(c)
    d = sum(c)
    print(d)
    return d