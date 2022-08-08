def solution(answers):

    first_=[1,2,3,4,5]
    second_=[2,1,2,3,2,4,2,5]
    third_=[3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3=0,0,0
    # answer은 순서대로 가면 되니까...
    for i in range(len(answers)):
        s1=i%5
        s2=i%8
        s3=i%10

        if first_[s1]==answers[i]:
            c1+=1
        if second_[s2]==answers[i]:
            c2+=1
        if third_[s3]==answers[i]:
            c3+=1

    k=max(c1,c2,c3)
    answer = []

    if k==c1:
        answer.append(1)
    if k==c2:
        answer.append(2)
    if k==c3:
        answer.append(3)



    return answer