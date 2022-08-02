def solution(n):
    answer = 0
    list_=list(str(n))
    print(list_)
    list_.sort(reverse=True)
    answer=int(''.join(list_))
    return answer