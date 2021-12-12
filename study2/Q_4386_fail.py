# 별자리
# fail!

import math

n=int(input())
xy=[]
for _ in range(n):
    xy.append(list(map(float, input().split())))

dif=[[],[],[]]

for i in range(n):
    for j in range(n):
        x=xy[i][0]-xy[j][0]
        y=xy[i][1]-xy[j][1]
        dif[i].append(math.sqrt(x**2+y**2))

print(dif)