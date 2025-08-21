

N = int(input())  


for _ in range(N):
    s= input()
    stack = []

    for a in s:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if len(stack) == 0:   #stack이 비어있지 않다면 True로 간주, 비어있으면 false
                stack.append(a)
                break
            else :
                stack.pop()
                

    if not stack:  #stack이 비어있다면
        print("YES")
    else :
        print("NO")