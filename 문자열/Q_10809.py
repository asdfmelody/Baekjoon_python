#알파벳찾기
# a 97     z 122
asc=[chr(i) for i in range(97,123)] #26개
arr=[-1 for i in range(97,123)]
word=input()
for a in range(len(word)):
    for b in range(26):
        if word[a] == asc[b]:
            if arr[b] == -1: #중복된 문자 처리
               arr[b] = a

for d in range(26):
    print(arr[d], end=(" ")) #한줄로 띄어쓰기하여 출력