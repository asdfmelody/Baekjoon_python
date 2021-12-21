# 5와 6의 차이
A,B=input().split()
minA, maxA, minB, maxB="", "","", ""
for i in range(len(A)):
    if int(A[i])== 5 or int(A[i])== 6 :
        minA+="5"
        maxA+="6"
    else:
        minA+=A[i]
        maxA+=A[i]
for i in range(len(B)):
    if int(B[i])== 5 or int(B[i])== 6 :
        minB+="5"
        maxB+="6"
    else:
        minB+=B[i]
        maxB+=B[i]


print(int(minA)+int(minB) , int(maxA)+int(maxB))