#크로아티아 알파벳
word=input()
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    word = word.replace(i,'*') #replace 함수..
print(len(word))

# 런타임 에러 났음 :
# word=input()
# count=0
# arr=list(word)
# i=0
# while(i<len(word)):
#     #print(i)
#     count+=1
#     if arr[i] == 'c':
#         if arr[i+1] == '-' or '=':
#             i+=1
#     elif arr[i] == 'd':
#         if arr[i+1] == 'z' and arr[i+2] == '=' :
#             i+=2
#         elif arr[i+1] =='-': i+=1
#     elif arr[i] == 'l':
#         if arr[i+1]=='j': i+=1
#     elif arr[i] == 'n':
#         if arr[i+1]=='j': i+=1
#     elif arr[i] == 's':
#         if arr[i+1]=='=': i+=1
#     elif arr[i] == 'z':
#         if arr[i+1]=='=': i+=1
#     i+=1
# print(count)