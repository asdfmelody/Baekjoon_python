# 분해합
def bunahap(M):
    N=M
    strM=str(M)
    for i in strM:
        N+=int(i)
    return N

N=int(input())

for i in range(N):
    result=0
    if N == bunahap(i) :
        result=i
        break

print(i)
