# 일곱 난쟁이
# 3kg 5kg 문제랑 비슷한 느낌
fake_nanjang=[]
for _ in range(9):
    fake_nanjang.append(int(input()))

heightsum=sum(fake_nanjang)

for i in range(9):
    for j in range(i+1,9):
        mustbe100=0
        mustbe100=heightsum-fake_nanjang[i]-fake_nanjang[j]
        if mustbe100 == 100:
            del fake_nanjang[j]
            del fake_nanjang[i]
            #print("found it")
            break
    if mustbe100 == 100: break

for i in sorted(fake_nanjang):
    print(i)