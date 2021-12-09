# IOIOI
# fail

N=int(input())
M=int(input())
S=input()

count=0

PN="I"
for i in range(N):
    PN+="OI"

PNlen= 1+N*2

# PNarr=(["I"]*100).append(["OI"*i for i in range(1,101)])
for i in range(M-PNlen):
    if PN == S[i:i+PNlen]:
        count+=1

print(count)