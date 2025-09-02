import sys


deque = []

N = int(input())

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push_back":
        deque.append(order[1])
    if order[0] == "push_front":
        deque.insert(0, order[1])
    if order[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            value = deque[-1]
            print(value)
            del deque[-1]
    if order[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            value = deque[0]
            print(value)
            del deque[0]
    if order[0] == "size":
        print(len(deque))    
    if order[0] == "empty":
        if deque:
            print(0)
        else: print(1)    
    if order[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if order[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
        