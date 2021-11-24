#숫자의 합
a=int(input())
intlist = list(map(int, str(input())))  # 정수의 각자리수를 list 형태로 저장
print(sum(intlist))