# 로프
N=int(input())
rope=[]
for i in range(N):
    rope.append(int(input()))

rope=sorted(rope)
weight=[]
for i in range(N):
    weight.append(rope[i]*(N-i))

print(max(weight))