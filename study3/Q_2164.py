# 카드2
import sys
input=sys.stdin.readline
N=int(input())

arr = [i+1 for i in range(N)]
while len(arr)>1:
    if len(arr) %2 ==0:
        arr=arr[1::2]
    else :
        t=[arr[-1]]
        t.extend(arr[1::2])
        arr=t

print(arr[0])