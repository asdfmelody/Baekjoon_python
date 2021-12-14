# 카드
import sys
input=sys.stdin.readline

N=int(input())
dic={}
for i in range(N):
    num=int(input)
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1