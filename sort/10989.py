import sys
input=sys.stdin.readline

n=int(input())
num=[0]*10001
for i in range(n):
  a=int(input())
  num[a]=num[a]+1

for i in range(10001):
  if num[i]!=0:
    for j in range(num[i]):
      print(i)
#메모리 초과 나지 않게 주의!
