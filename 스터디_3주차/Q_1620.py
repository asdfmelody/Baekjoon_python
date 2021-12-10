# 나는야 포켓몬 마스터 이다솜

import sys
input=sys.stdin.readline # input() -> sys.stdin.readline()

N,M=map(int,input().split())

dogam={} #dictionary 이용하면 list append 보다 빠름

for i in range(1,N+1):
    name=input().rstrip() # 문자열 입력받을때 .rstrip()
    dogam[i]=name
    dogam[name]=i

for _ in range(M):
    Q=input().rstrip()
    if Q.isdigit() :
        print(dogam[int(Q)])
    else:
        print(dogam[Q])
