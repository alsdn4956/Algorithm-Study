
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result = 0

S = input()

for s in S:
    for j in dial :
        if s in str(j) :
            num = dial.index(j) +3
            result += num            
            
print(result)
