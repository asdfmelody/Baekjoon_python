#그룹 단어 체커
word=input()

for i in range(len(word)):
    if word[i] == word[i+1]:
        word=word[:i]+word[i]+word[i+2:]

print(word)