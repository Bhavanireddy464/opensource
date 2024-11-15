n=int(input())
m1=[]
for _ in range(n):
    row=list(map(int,input().split()))
    m1.append(row)
for i in range(n):
    m1[i]=m1[i][::-1]
for row in m1:
    for num in row:
        print(num, end=' ')
    print()
