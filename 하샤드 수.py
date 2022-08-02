# class Solution {
# public boolean solution(int x) {
# boolean answer = false;
# int k=0;
# int input= x;
# int sum=0;
# while(input!=0){
# k=input%10;
# sum+=k;
# input/=10;
#
# }
#
# if(x%sum==0){
# answer=true;
# }
# return answer;
# }
# }