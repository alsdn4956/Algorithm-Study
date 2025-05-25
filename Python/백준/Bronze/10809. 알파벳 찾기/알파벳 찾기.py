S = input()
word = 'abcdefghijklmnopqrstuvwxyz'

for x in word:
    if x in S :
        print(S.index(x), end=' ')
    else:
        print(-1, end=' ')
        



# word에 알파벳 단어 넣고 S 단어 있는 것에 프린트?
# 