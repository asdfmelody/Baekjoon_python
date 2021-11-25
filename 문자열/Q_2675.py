#문자열 반복
def repeat_letter():
    repeat,word=input().split() #한번에 값 두개 입력
    result=""
    for c in range(len(word)):
        result+=word[c]*int(repeat) #문자열은 append 사용 안함
    return(result)

time= int(input())
arr=["" for i in range(time)]
for i in range(time):
    arr[i]=repeat_letter()

for i in range(time):
    print(arr[i])

