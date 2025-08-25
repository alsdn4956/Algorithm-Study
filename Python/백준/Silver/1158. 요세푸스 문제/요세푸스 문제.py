N, K = map(int,input().split())


queue = []


for i in range(1, N+1):
    queue.append(i)
    
    
idx = 0
result = []   
    
while len(queue) > 0:
    idx = (idx + K-1) % len(queue) #원형 순환 인덱스 계산
    value = queue[idx]
    result.append(value)
    del queue[idx]
    
print("<" + ", ".join(map(str, result)) + ">")
    


