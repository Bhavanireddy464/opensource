n,x,y=map(int,input().split())
if (y >= n*(x-1)) and y <= n*x and y % x == 0:
    print("YES")
else:
    print("NO")
