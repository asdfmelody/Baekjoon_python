# 암호
from itertools import combinations
import sys
input = sys.stdin.readline
L,C=map(int,input().split())
arr=sorted(list(input().split()))

word=sorted(set(map("".join,combinations(arr, L)))) # nPr 경우의수를 문자열 형식으로 변환 후 set 으로 중복제거

for i in word:
    moum=0 # 모음 개수
    jaum=0 # 자음 개수
    for j in range(L):
        if i[j] in "aeiou": # 모음있으면
            moum+=1
        else:
            jaum+=1

        if moum >=1 and jaum >=2:
            print(i)
            break
