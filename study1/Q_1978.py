#소수 찾기

a=int(input())
arr=list(map(int, input().split()))
result=len(arr)
for i in range(len(arr)):
    if arr[i] == 1 : result-=1
    elif arr[i] > 1 :
        for j in range(2,arr[i]):
            if arr[i]%j == 0:
                result-=1
                break

print(result)

#for문 2개 -> 2제곱