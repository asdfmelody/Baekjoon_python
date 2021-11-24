# WIL(What I Learned)
모르는 것을 학습함에 있어서 매일(Today)에 집중하기 보다 무엇(What)을 배웠는지에 집중하기로 한다.

## 1. 1차원 배열
### 1.1 set 함수를 이용한 중복제거

>#### [Q_3052.py](https://www.acmicpc.net/problem/3052)
>수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.   
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
<pre><code>arr=[]
for a in range(10):
    arr.append(int(input())%42)

print(len(set(arr)))
</code></pre>

set() 함수로 배열 변환하여 집합 자료형으로 만들어준다.   
집합자료형은 중복제거 되어 생성되기 때문에 **중복제거를 위한 필터링** 으로 이용


### 1.2 list 함수로 한글자씩 끊어서 배열만들기
#### 1.2.1 문자열

>#### [Q_8958.py](https://www.acmicpc.net/problem/8958)
>OXOOX와 같은 **문자열**을 입력받아 퀴즈 점수 구하기
<pre><code>arr = list(input())

# 입력 : OXOOX    
# 출력 : >> ['O', 'X', 'O', 'O', 'X']
</code></pre>
#### 1.2.2 띄어쓰기로 구분된 정수형
>#### [Q_1546.py](https://www.acmicpc.net/problem/1546)
>평균 점수 구하기
<pre><code>arr = list(map(int,input().split()))

# 입력 : 40 60 80    
# 출력 : >> [40, 60, 80]
</code></pre>

### 1.3 round 함수
> #### [Q_4344.py](https://www.acmicpc.net/problem/4344)
> 반올림하여 소수점 셋째 자리까지 출력
<pre><code>result = round(float_number,3)
</code></pre>
**round(대상값)**   
**round(대상값, 자릿수)**     

### 1.4 숫자와 함께 "%"를 출력하고 싶을때
> #### [Q_4344.py](https://www.acmicpc.net/problem/4344)
> 입력 : 70 90 80   
> 출력 : >>33.333%
<pre><code>print( "%0.3f%%" % result)
</code></pre>
세번째 자리까지 float형인 result를 문자열 "%"와 함께 출력   
~~print(result+"%")~~


## 2. 함수
### 2.1 정수의 각자리 숫자를 list로

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수
<pre><code>intlist=list(map(int, str(a)))
</code></pre>
정수를 string으로 바꾸고 int 형으로 list 만들기

### 2.2 길이가 정해진 리스트 만들기

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하라
<pre><code>arr=[False for i in range (10001)]
</code></pre>
length가 10000 인 list 만들고 모두 False 로 채움    
[False, False, False, ..., False]

### 2.3 Boolean list의 index값 이용

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>셀프넘버 문제
<pre><code>for b in range(10000):
    if arr[b] != True : print(b)
</code></pre>
arr는 boolean list이고 True가 아닌 list index를 출력한다.

## 3. 문자열
### 3.1 아스키코드와 문자
>#### [Q_11654.py](https://www.acmicpc.net/problem/11654)
> 문자를 아스키코드로 변환하기
<pre><code>ord('A')     >> 65  # 문자->아스키 ord()
char('65')   >> A   # 아스키->문자 char()
</code></pre>


### 3.2 end=(" ")
>#### [Q_10809.py](https://www.acmicpc.net/problem/10809)
> 배열 출력시 한줄로 띄어쓰기 출력
<pre><code>for d in range(26):
    print(arr[d], end=(" ")) </code></pre>