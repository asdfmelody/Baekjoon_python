# 피보나치 함수
# dp
dp=[0,0]*41 # N 40 이하

def fibo(n):
    if n==0 : return [1,0]
    elif n==1: return [0,1]
    elif dp[n] !=0: return dp[n]
    dp[n] = [x+y for x,y in zip(fibo(n-1),fibo(n-2))]
    # 리스트끼리 더하기 c=[x+y for x,y in zip(a,b)]
    return dp[n]

T=int(input())
N=[]
for i in range(T):
    N.append(int(input()))

for i in range(T):
    print(fibo(N[i])[0],fibo(N[i])[1])