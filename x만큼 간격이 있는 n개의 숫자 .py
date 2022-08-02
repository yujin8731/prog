def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i+1))
    return answer

'''class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long [n];
        
        for(int i=0;i<n;i++){
                answer[i]=x*(i+1);
        }
        return answer;
    }
}'''