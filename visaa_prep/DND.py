n,m=map(int,input().split())
arr = list(map(int,input().split()))
num1=0
num2=0
for i in arr:
    if i%m == 0:
        num2 += i
    else:
        num1 += i
p=num2-num1
print(p)
