import sys
input=sys.stdin.readline

N=int(input())
distance=list(map(int,input().split()))
cost=list(map(int,input().split()))
result=0

min=cost[0]
for i in range(len(distance)):
    if min > cost[i] : min = cost[i]
    result+=min*distance[i]

print(result)