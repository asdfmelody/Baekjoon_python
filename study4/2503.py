#숫자 야구

from itertools import permutations

# candidate: 영수가 생각한 숫자, guess: 민혁이가 추측한 숫자
def check(candidate, guess): # strike 와 ball 출력하는 함수
    strike, ball, nothing=0,0,0
    for i in range(3):
        if candidate[i] == guess[i] : strike +=1 # strike 확인 하기
        elif candidate[i] not in guess : nothing+=1# strike ball 도 아닐때
    ball=3-nothing-strike
    return(strike, ball)


numbers=[str(i+1) for i in range(9)] # 1~9
candidate=list(map("".join,permutations(numbers,3))) # 정답 가능성 있는 후보 - str으로 만들기

N=int(input())

for i in range(N):
    int_guess, strike, ball = map(int,input().split())
    guess=str(int_guess)
    new_candidate=[] # 새로운 후보군 선언
    for j in candidate:
        c_strike, c_ball=check(j,guess) # check 함수 사용
        if c_strike==strike and c_ball == ball : #check 함수랑 같으면
            new_candidate.append(j) # 새로운 후보군 리스트에 추가
    candidate=new_candidate

print(len(candidate))

