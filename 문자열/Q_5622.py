#다이얼
# 3~10초 / 버튼2~9
arr=['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=list(input())
count=0
for i in range(len(word)):
    for a in range(8):
        if word[i] in arr[a] :
            count+=a+3
print(count)