# 수강신청
# fail
import sys

input=sys.stdin.readline

K,L=map(int,input().split())
dic={}
for i in range(L):
    num=input().rstrip()
    dic[num]=i

sdic=dict(sorted(dic.items(), key=lambda x:x[1]))
# 딕셔너리 value값으로 sort하기,,
key=list(sdic.keys()) # key 리스트 만들기

for j in range(K):
    print(key[j])