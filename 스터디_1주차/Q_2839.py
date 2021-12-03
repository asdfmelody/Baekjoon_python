# 설탕 배달
sugar=int(input())
five=int(sugar/5)
number=[]
for i in range(five+1): #0~3
    if i==0 and sugar%3==0:
        number.append(int(sugar/3))
    if i>0 and (sugar-i*5)%3 == 0 :
        three=int((sugar-i*5)/3)
        number.append(i + three)

if len(number) >0 : print(min(number))
else : print(-1)

#greedy 방식

#dp로 풀어보기