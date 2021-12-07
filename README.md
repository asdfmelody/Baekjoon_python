# WIL(What I Learned)
모르는 것을 학습함에 있어서 매일(Today)에 집중하기 보다 무엇(What)을 배웠는지에 집중하기로 한다.

## 목차
1. [1차원 배열](#1-1차원-배열)
1. [함수](#2-함수)
1. [문자열](#3-문자열)
1. [동적 프로그래밍](#4-동적-프로그래밍Dynamic-Programming)
-----

## 1. 1차원 배열
### 1.1 set 함수를 이용한 중복제거

>#### [Q_3052.py](https://www.acmicpc.net/problem/3052)
>수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.   
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
```python
arr=[]
for a in range(10):
    arr.append(int(input())%42)

print(len(set(arr)))
```

set() 함수로 배열 변환하여 집합 자료형으로 만들어준다.   
집합자료형은 중복제거 되어 생성되기 때문에 **중복제거를 위한 필터링** 으로 이용


### 1.2 list 함수로 한글자씩 끊어서 배열만들기
#### 1.2.1 문자열

>#### [Q_8958.py](https://www.acmicpc.net/problem/8958)
>OXOOX와 같은 **문자열**을 입력받아 퀴즈 점수 구하기
```python
arr = list(input())

# 입력 : OXOOX    
# 출력 : >> ['O', 'X', 'O', 'O', 'X']
```
#### 1.2.2 띄어쓰기로 구분된 정수형
>#### [Q_1546.py](https://www.acmicpc.net/problem/1546)
>평균 점수 구하기
```python
arr = list(map(int,input().split()))

# 입력 : 40 60 80    
# 출력 : >> [40, 60, 80]
```

### 1.3 round 함수
> #### [Q_4344.py](https://www.acmicpc.net/problem/4344)
> 반올림하여 소수점 셋째 자리까지 출력
```python
result = round(float_number,3)
```
**round(대상값)**   
**round(대상값, 자릿수)**     

### 1.4 숫자와 함께 "%" 출력 : print( "%0.3f%%" % result)
> #### [Q_4344.py](https://www.acmicpc.net/problem/4344)
> 입력 : 70 90 80   
> 출력 : >>33.333%
```python
print( "%0.3f%%" % result)
```
세번째 자리까지 float형인 result를 문자열 "%"와 함께 출력   
~~print(result+"%")~~

------
## 2. 함수
### 2.1 정수의 각 자리 숫자를 list로 

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수
```python
intlist=list(map(int, str(a)))
```
**list(map(int,str(a)))**
정수를 string으로 바꾸고 int 형으로 list 만들기

### 2.2 길이가 정해진 리스트 만들기

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하라
```python
arr=[False for i in range (10001)]
```
length가 10000 인 list 만들고 모두 False 로 채움    
[False, False, False, ..., False]

### 2.3 Boolean list의 index값 이용

>#### [Q_4673.py](https://www.acmicpc.net/problem/4673)
>셀프넘버 문제
```python
for b in range(10000):
    if arr[b] != True : print(b)
```
arr는 boolean list이고 True가 아닌 list index를 출력한다.

------

## 3. 문자열
### 3.1 아스키코드와 문자 : ord('A') char('65')
>#### [Q_11654.py](https://www.acmicpc.net/problem/11654)
> 문자를 아스키코드로 변환하기
```python
ord('A')     >> 65  # 문자->아스키 ord()
chr(65)      >> A   # 아스키->문자 chr()
```

### 3.2 end=(" ")
>#### [Q_10809.py](https://www.acmicpc.net/problem/10809)
> 배열 출력시 한줄로 띄어쓰기 출력
```python
for d in range(26):
    print(arr[d], end=(" "))
```

### 3.3 문자열은 append 대신 +=
>#### [Q_2675.py](https://www.acmicpc.net/problem/2675)
> +=로 문자열 연장
```python
for c in range(len(word)):
    result+=word[c]*int(repeat)
```
append 이용 시 오류 메시지: ‘str’ object has no attribute ‘append’

### 3.4 대문자로 변환 : upper() capitalize() title()
>#### [Q_1157.py](https://www.acmicpc.net/problem/1157)
> 입력데이터는 대소문자 구별X, 출력시 대문자로만 출력
```python
word=input().upper()
```
대문자 변환 메소드는 총 **세가지**

```python
string.upper() #모든 알파벳 대문자로 변환
string.capitalize() #첫 글자를 대문자로 변환
string.title() #알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 
                나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환
```

**소문자로 변환**하는 메소드는 한가지
```python
string.lower() #모든 알파벳 소문자로 변환
```
### 3.5 문자열 변경 : replace(old_str, new_str)
>#### [Q_2941.py](https://www.acmicpc.net/problem/2941)
> 크로아티아 알파벳 갯수 세기
```python
word=input()
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    word = word.replace(i,'*') #word내에 cro 있다면 '*' 로 바꾸기
print(len(word))
```
**문자열 변경**하는 함수 - 긴 문자열을 한덩이로 구분하여 갯수 구할때 이용 가능

-------

## 4. 동적 프로그래밍 (Dynamic Programming)
분할정복 기법: 큰 문제를 한 번에 해결하기 힘들 때 작은 여러개의 문제로 나누어 푸는 기법
### 4.1 막대기 자르기
> 길이(i) 0 1 2 3 4 5 6 7 8 9 10   
가격(Pi) 0 1 5 8 9 10 17 17 20 24 30 
> 
> => 길이가 n인 막대기의 최대 가격을 Rn이라고 했을 때, Rn = max(Pi + Rn-i) (i는 1부터 n)

**Rn = max(Pi + Rn-i)**   
- R1은 1   
- R2는 max(P1 + R1, P2 + R0) = max(2, 5) = 5    
- R3는 max(P1 + R2, P2 + R1, P3 + R0) = max(6, 6, 8) = 8    
- R4는 max(9, 10, 9, 9) = 10   

```python
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cutRod(p, n):
  r = [0]
  for j in range(1,n+1):
    q = -1
    for i in range(1,j+1):
      q = max(q, p[i] + r[j - i])
    r.append(q)
  return r[n]

cutRod(p, 2); # 5
cutRod(p, 3); # 8
cutRod(p, 4); # 10
cutRod(p, 7); # 18
```

### 4.2 최장 공통 부분 수열 문제

### 4.3 0/1 배낭 문제


