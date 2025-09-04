S = input().strip() + ' ' #마지막에 공백 추가

result = ''
stack = []
cnt = 0

for i in S:
    if i == '<':
        cnt = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)
        
        
        
    if i == '>':
        cnt = 0
        for _ in range(len(stack)):
            result+= stack.pop(0)
        

    if i == ' ' and cnt == 0:
        stack.pop() # 들어ㅏ간 공백 빼주기
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

print(result)        