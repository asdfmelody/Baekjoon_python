# 영역구하기
from collections import deque

queue=deque()
cnt=[]

M,N,K=map(int,input().split())
monun=[[0 for col in range(N)] for row in range(M)] # [[0]*N]*M 하면 shallow copy,,

for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(M-y2, M-y1):
            monun[y][x]=1 # 색칠된 부분 1로

dy=[-1,1,0,0]
dx=[0,0,-1,1]

for x in range(M):
    for y in range(N):
        if monun[x][y] == 0:
            monun[x][y] = 2 # 방문한건 2로!
            count=1
            queue.append((x,y))
            while queue: # queue가 빌때 까지 반복
                x,y=queue.popleft()
                for i in range(4): # 4방향으로 위치 확인
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if nx < 0 or nx>=M or ny<0 or ny>=N: # 벽일때
                        continue
                    elif monun[nx][ny] == 0:
                        monun[nx][ny] = 2 # 방문한건 2로!
                        queue.append((nx,ny))
                        count+=1
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=" ")