# class Solution {
# public int solution(int num) {
# int answer = 0;
# int cnt=0;
#
# if (num==1){
# return 0;
# }
#
#
# while (true){
# if (num==1){
# break;
# }
# if (cnt==500){
# break;
# }
# if (num%2==0){
# num/=2;
# cnt++;
# }
# else{
# num=num*3+1;
# cnt++;
# }
# }
#
#
# if (cnt>=500){
# answer=-1;
# }
# else{
# return cnt;
# }
#
# return answer;
# }
# # }