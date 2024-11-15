t=int(input())
for _ in range(t):
    x , n = map(int,input().split())
    y=x//10
    n= y * n
    print(n)
