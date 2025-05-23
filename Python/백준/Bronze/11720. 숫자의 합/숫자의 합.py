N=int(input())

M = list(map(int, input()))

numbers = 0
for i in range(N):
    numbers+= M[i]
    
    
print(numbers)