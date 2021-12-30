# 결혼식
from collections import deque

n=int(input())
m=int(input())
friend=[[] for i in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    friend[x].append(y)
    friend[y].append(x)

list=[0]*(n+1)
list[1]=1

queue=deque()
queue.append(1)
while queue:
    node=queue.popleft()
    for i in friend[node]:
        if list[i]==0:
            list[i]=list[node]+1
            queue.append(i)
result=0
for i in list:
    if i==2 or i==3:
        result+=1
print(result) # 2 이상 3 이하 2,3인것만
print(list)
# 연결 2개까지,, = 깊이 제한
