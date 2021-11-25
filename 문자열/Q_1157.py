#단어공부
#A 65          Z 90
arr=[0 for i in range(26)]
word=input().upper() #모든 문자 대문자로
for i in range(len(word)):
    arr[ord(word[i])-65]+=1

count=0
for a in range(26):
    if arr[a] == max(arr) :
        count+=1
        result=chr(a+65)

if count ==1: print(result)
else: print("?")
