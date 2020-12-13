import sys

input=sys.stdin.readline
n,m,k=map(int, input().split())
dp=[[0]*(m+1) for _ in range(n+1)]
dp[0][1]=1
temp=1

for i in range(1, n+1):
  for j in range(1, m+1):
    dp[i][j]=dp[i-1][j]+dp[i][j-1]
    if k==temp:
      kx = i
      ky = j
    temp+=1

if k==0:
  print(dp[n][m])
else:
  print(dp[kx][ky]*dp[n+1-kx][m+1-ky])
