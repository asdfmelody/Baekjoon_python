#상수

def reverse(word):
    a=int(word/100)
    b=int(word/10-a*10)
    c=word%10
    return int(a+10*b+100*c)

a,b=input().split()
rev_a=reverse(int(a))
rev_b=reverse(int(b))
if rev_a>rev_b:
    print(rev_a)
else: print(rev_b)