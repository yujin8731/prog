def solution(phone_number):
    answer = ''

    #     for i in range(len(str(phone_number))-4):
    #         answer+='*'

    #     answer+= phone_number[-4:]
    for i in range(len(str(phone_number))):
        if i<(len(str(phone_number))-4):
            answer+='*'
        else:
            answer+=phone_number[i]

    return answer