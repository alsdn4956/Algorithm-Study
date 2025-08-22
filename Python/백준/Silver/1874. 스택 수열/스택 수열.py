N = int(input())

stack=[]
now=1
answer = []
find = True



for _ in range(N):
    s = int(input())
    while now <= s:
        stack.append(now)
        answer.append("+")  
        now +=1

    if stack[-1] == s:
        stack.pop()
        answer.append("-")
    else:
        find = False
        
        
if not find:
    print("NO")
else :
    for i in answer:
        print(i)