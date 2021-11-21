# Baekjoon_python
# 정리 메모


## 1. 1차원 배열

# WIL(What I Learned)
모르는 것을 학습함에 있어서 매일(Today)에 집중하기 보다 무엇(What)을 배웠는지에 집중하기로 한다.

## 1. 1차원 배열
### 1.1 set 함수를 이용한 중복제거

>#### Q_3052.py   
>수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.   
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
<pre>
<code>
arr=[]
for a in range(10):
    arr.append(int(input())%42)

print(len(set(arr)))
</code>
</pre>

set() 함수로 배열 변환하여 집합 자료형으로 만들어준다.   
집합자료형은 중복제거 되어 생성되기 때문에 **중복제거를 위한 필터링** 으로 이용


### 1.2 list 함수로 한글자씩 끊어서 배열만들기
#### 1.2.1 문자열

>#### Q_8958.py   
>OXOOX와 같은 **문자열**을 입력받아 퀴즈 점수 구하기
<pre>
<code>
arr = list(input())

# 입력 : OXOOX    
# 출력 : >> ['O', 'X', 'O', 'O', 'X']
</code>
</pre>
#### 1.2.2 띄어쓰기로 구분된 정수형
>#### Q_1546
>평균 점수 구하기
<pre>
<code>
arr = list(map(int,input().split()))

# 입력 : 40 60 80    
# 출력 : >> [40, 60, 80]
</code>
</pre>