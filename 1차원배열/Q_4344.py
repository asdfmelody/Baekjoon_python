#평균은 넘겠지

many=int(input())
case=[]
result=[]
for a in range(many):
    case.append(list(map(int,input().split())))
    students=case[a][0]
    avg=(sum(case[a])-students)/students #arr[0]로 하는게 더 빠른지 students 선언해서 배정해주는게 빠른지

    count=0
    for i in range(1,students+1):
        if case[a][i]>avg : count +=1

    result.append(round((float)(count/students*100),3)) #round 함수

for a in range(many):
    print( "%0.3f%%" % result[a]) #float함수 출력과 문자열"%" 출력방법

