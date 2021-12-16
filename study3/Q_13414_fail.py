# 수강신청
# fail 시간초과
import sys
# import queue
input=sys.stdin.readline

K,L=map(int,input().split())
arr=[]
for _ in range(L):
    num=input().rstrip()
    if num in arr:
        arr.remove(num) # queue는 remove하면 no! append,pop을 해야 유용
    arr.append(num)

for i in range(K):
    print(arr[i])
