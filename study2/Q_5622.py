# 다이얼

Dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #3~9초 +3
input=input()
second=0

for i in range(len(input)):
    for j in range(8):
        if input[i] in Dial[j]:
            second+=j+3
            break

print(second)