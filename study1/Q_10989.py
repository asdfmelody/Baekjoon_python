# 수 정렬하기3
# 메모리 초과 ) append 이용시 메모리 재할당 -> 효율적 사용 불가

import sys

n = int(sys.stdin.readline()) # 시간 초과 ) readline으로 입력받기
n_list = [0] * 10001

for _ in range(n): # index 필요 없을때 _ 이용
    n_list[int(sys.stdin.readline())] +=1

for i in range(10001):
    if n_list[i] !=0:
        for j in range(n_list[i]):
            print(i)

