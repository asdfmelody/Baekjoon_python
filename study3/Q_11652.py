# 카드
import sys
input=sys.stdin.readline

N=int(input())
dic={}
for i in range(N):
    num=int(input())
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1

sdic=sorted(dic.items(), key=lambda x: (-x[1],x[0])) # value 의 오름차순, key 의 내림차순

print(sdic[0][0])