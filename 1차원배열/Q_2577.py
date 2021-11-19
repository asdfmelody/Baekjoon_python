#숫자의 개수
result=1
for i in range(3):
    result *= int(input())

arr=[0,0,0,0,0,0,0,0,0,0]
for s in str(result):
    arr[int(s)] +=1

for a in range(len(arr)):
    print(arr[a])
