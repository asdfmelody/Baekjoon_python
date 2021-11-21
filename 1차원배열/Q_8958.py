#OX퀴즈
many=int(input())

arr=[]
for a in range(many):
    arr.append(list(input()))  # 문자열 하나씩 자르기 list

for a in range(many):
    result = 0
    count = 0
    for i in range(len(arr[a])):
        if arr[a][i] == 'O':
            count +=1
        else :count=0
        result+=count
    print(result)