one, two, three = map(int, input().split())


if one == two == three:  # 같은 눈이 3개
    prize = 10000 + one * 1000
elif one == two or one == three:  # 같은 눈이 2개 (one이 포함)
    prize = 1000 + one * 100
elif two == three:  # 같은 눈이 2개 (two와 three가 같음)
    prize = 1000 + two * 100
else:  # 모두 다른 눈
    prize = max(one, two, three) * 100

print(prize)
