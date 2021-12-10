# 패션왕 신해빈
T=int(input())

def case(n):
    dic={}
    result=1
    for _ in range(n):
        name, kind =input().split()
        if kind in dic: # 이미 종류가 등록되어있으면
            dic[kind] = dic[kind]+1 # 원래 값에 1 추가
        else: dic[kind] =1 # 등록 안되어 있으면 1로 초기화
    dic_val=list(dic.values()) # 갯수들로만 이루어진 list 만들기

    for i in range(len(dic_val)):
        result*=dic_val[i]+1 # [2,1] 이면 result = 3*2
    print(result-1) # 알몸인 경우 -1

for _ in range(T):
    n=int(input())
    case(n)