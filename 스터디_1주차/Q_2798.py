# 블랙잭
n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum_arr=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            sum=arr[i]+arr[j]+arr[k]
            if sum<=m :
                sum_arr.append(sum)

print(max(sum_arr))