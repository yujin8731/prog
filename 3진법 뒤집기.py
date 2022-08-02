def solution(n):
    a=''
    while True:
        a=str(n%3)+a
        n=n//3
        if n==0:
            break
    answer=0
    for i in range(len(a)):
        answer+=int(a[i])*3**i

    return answer