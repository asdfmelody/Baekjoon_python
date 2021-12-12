# 좌표 정렬하기
N=int(input())
arr=[]
for i in range(N):
    x,y=map(int, input().split())
    arr.append([x,y])

arr.sort()

for i in range(N):
    print(str(arr[i][0])+" "+str(arr[i][1]))
    # print(arr[i][0],arr[i][1]) 로도 가능
    # https://www.acmicpc.net/source/36172885
    # 보면 마지막 print 줄 다르게 할수 있다.