def d(a):
    result=a
    intlist=list(map(int, str(a))) #정수의 각자리수를 list 형태로 저장
    result+=sum(intlist)
    return result

#boolean list의 index값 이용 1~10000
arr=[False for i in range (10001)] #길이가 정해진 리스트 만들기
for a in range(10000):
    if d(a) <=10000:
        arr[d(a)]=True
for b in range(10000):
    if arr[b] != True : print(b)
