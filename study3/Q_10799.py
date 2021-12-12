# 쇠막대기
bar=input()
result=0
count = 0 # 겹쳐있는 막대기 개수 (층)

i=0
while i<len(bar):
    if bar[i] == "(":
        count+=1
        if bar[i+1] ==")": # lazer
            count-=1
            result+=count
            i+=1
    elif bar[i] ==")" and count>0:
        count-=1
        result+=1
    i += 1

print(result)