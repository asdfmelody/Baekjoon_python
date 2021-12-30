# 바이러스

def check(a):
    for i in network[a]:
        if list[i] == 1:
            list[i] = 2
            check(i)

n= int(input())
r=int(input())

network=[[] for i in range(n+1)] # [[],[],[],..]
for _ in range(r):
    x,y=map(int,input().split())
    network[x].append(y)
    network[y].append(x)

list=[1]*(n+1) #[0,0,0,0,0,0,..]

check(1)

result=-1
for i in list:
    if i ==2 :
        result+=1
print(result)
