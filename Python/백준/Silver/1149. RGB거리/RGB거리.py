T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]
dp = [[0,0,0] for _ in range(T)] 




dp[0][0] = lst[0][0]
dp[0][1] = lst[0][1]
dp[0][2] = lst[0][2]
for i in range(1, T):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + lst[i][0]
    dp[i][1] = min(dp[i-1][2],dp[i-1][0]) + lst[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + lst[i][2]
print(min(dp[T-1]))
