def solution():
    n = int(input())
    rope = []
    for i in range(n):
        rope.append(int(input()))
    rope.sort(reverse=True)
    for j in range(n):
        rope[j] = rope[j] * (j+1)
    return max(rope)

print(solution())
