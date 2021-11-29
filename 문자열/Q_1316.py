# 그룹 단어 체커
# 다시 풀어보기
group_count=n=int(input())

for i in range(n):
    word=input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]: # 다를때
            if word[j+1] in word[:j]: # 지금 알파벳과 이전까지의 알파벳 비교
                group_count-=1
                break
print(group_count)