import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mylist = list(map(int, input().split()))

Ssum = [0]

temp =0

for i in mylist:
    temp += i
    Ssum.append(temp)
    

for i in range(M):
    i, j = map(int, input().split())
    print(Ssum[j] - Ssum[i-1])

    
