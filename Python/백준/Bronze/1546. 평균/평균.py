N = int(input())
mylist = list(map(int, input().split()))

M = max(mylist)
scores =0

for i in mylist:
    scores += i / M * 100
    
print(scores/N)
    
