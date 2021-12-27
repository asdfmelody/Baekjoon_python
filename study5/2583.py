# 영역구하기
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def count(x,y):
    queue=deque()

    while queue: # queue가 빌때 까지 반복
        x,y=queue.popleft()
        for i in range(4): # 4방향으로 위치 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx>=N or ny<0 or ny>=M:
                continue
            if monun[nx][ny] >0:
                continue
            if monun[nx][ny] ==0:
                monun[nx][ny]=2 # 방문한건 2로!
                queue.append((nx,ny))
    return monun

M,N,K=map(int,input().split())
monun=[[0 for col in range(N)] for row in range(M)] # [[0]*N]*M 하면 shallow copy,,

for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(M-y2, M-y1):
            monun[y][x]=1

print(count(0,0))