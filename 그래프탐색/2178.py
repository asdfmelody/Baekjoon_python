# 미로 탐색
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue: # queue가 빌때 까지 반복
        x,y=queue.popleft()
        for i in range(4): # 4방향으로 위치 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

n,m=map(int, input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))