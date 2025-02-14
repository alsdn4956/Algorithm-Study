import sys

t = int(sys.stdin.readline())
sum = 0
for i in range(1,t+1):
    a, b = map(int, sys.stdin.readline().split())
    sum=a+b
    print("Case","#"+str(i)+":",sum)
    