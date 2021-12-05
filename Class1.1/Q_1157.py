# 단어 공부
# A 65     Z 90
word=input().upper()
count=[0] *26

for i in range(len(word)):
    count[ord(word[i])-65]+=1

a=0

for i in range(26):
    if max(count) == count[i] :
        a+=1
        result=chr(i+65)

if a==1: print(result)
else : print('?')