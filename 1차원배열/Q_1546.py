#평균
count=int(input())
arr=list(map(int,input().split()))

max=max(arr)

result=(float)(sum(arr)/max*100/count)

print(result)