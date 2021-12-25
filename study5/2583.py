# 영역구하기
M,N,K=map(int,input().split())
monun=[[0 for col in range(N)] for row in range(M)] # [[0]*N]*M 하면 shallow copy,,

for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(M-y2, M-y1):
            monun[y][x]=1

print(monun)