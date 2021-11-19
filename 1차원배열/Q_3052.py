#나머지

arr=[]
for a in range(10):
    arr.append(int(input())%42)

print(len(set(arr)))

# <set 함수로 만들기>
# 집합 자료형으로 만들어줌
# 중복제거를 위한 필터 역할..