#ACM 호텔
i=int(input())
result=[]
for a in range(i):
    h,w,n=map(int,input().split())
    if (n%h == 0) :
        floor=h
        ho=int(n/h)
    else:
        floor = n%h
        ho=int(n/h)+1
    result.append(ho+(floor*100)) #zfill 이용

for a in range(i):
    print(result[a])