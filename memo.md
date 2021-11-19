#메모

## 1. 1차원 배열
### 1.1 set 함수를 이용한 중복제거
<pre>
<code>
arr=[]
for a in range(10):
    arr.append(int(input())%42)

print(len(set(arr)))
</code>
</pre>

set() 함수로 배열 변환하여 집합 자료형으로 만들어준다.
집합자료형은 중복제거 되어 생성되기 때문에 