t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    unlucky_students= n - m
    if(unlucky_students>0):
        print(unlucky_students, end='\n')
    else:
        print(0)
