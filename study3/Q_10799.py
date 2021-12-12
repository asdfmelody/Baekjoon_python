# 쇠막대기
bar=input()
bar=bar.replace("()","0")
result=0
count = 0 # 겹쳐있는 막대기 개수 (층)

for i in bar:
    if i == "(":
        count+=1
    elif i=="0":
        result+=count
    else:
        count-=1
        result+=1

print(result)