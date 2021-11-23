#한수
def hansu(a):
    intlist=list(map(int, str(a))) #정수의 각자리수를 list 형태로 저장
    count=a
    if len(intlist) >= 3:
        #세자리 이상
        for t in range(100,a+1):
            intlist3=list(map(int, str(t)))
            for i in range(len(intlist3)-2):
                if(intlist3[i]-intlist3[i+1] != intlist3[i+1]-intlist3[i+2]):
                    count-=1
                    break
    return count

print(hansu(int(input())))