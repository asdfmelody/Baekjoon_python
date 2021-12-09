# Hashing
# -96

L=int(input())
word=input()
result=0

for i in range(L):
    result+=(ord(word[i])-96)*(31**i)

print(result%1234567891)