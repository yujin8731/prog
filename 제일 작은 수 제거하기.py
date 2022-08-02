def solution(arr):

    min_=arr[0]

    if len(arr)==1:
        return [-1]

    else:
        for i in range(len(arr)):
            if min_>arr[i]:
                min_=arr[i]
        arr.remove(min_)

    return arr