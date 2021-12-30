#촌수계산

def check(a):
    for i in chon[a]:
        if list[i] == 0:
            list[i] = list[a]+1
            check(i)

n= int(input())
p1, p2 = map(int,input().split())
r=int(input())

chon=[[] for i in range(n+1)] # [[],[],[],..]
for _ in range(r):
    x,y=map(int,input().split())
    chon[x].append(y)
    chon[y].append(x)

list=[0]*(n+1) #[0,0,0,0,0,0,..]
check(p1)
result=list[p2]
print(result if result>0 else -1)
