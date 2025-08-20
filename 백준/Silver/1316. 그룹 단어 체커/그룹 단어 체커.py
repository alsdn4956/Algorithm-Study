N = int(input())
result =0


for i in range(N):
    word = input()
    is_group = True


    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                is_group=False
                break
    if is_group == True:
        result += 1

print(result)