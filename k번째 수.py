def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        list_=array[commands[i][0]-1:commands[i][1]]
        list_.sort()
        answer.append(list_[commands[i][2]-1])
    return answer