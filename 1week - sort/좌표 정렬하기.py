N = int(input())
list = []


for i in range(N) :
    [x, y] = map(int, input().split())
    list.append([x, y])
list.sort()
for x in list:
    print(x[0], x[1])
