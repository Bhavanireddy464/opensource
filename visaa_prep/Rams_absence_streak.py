n=int(input())
a=list(map(int,input().split()))
ab=0
p=0
for i in a:
    if i==0:
        p += 1
        ab = max(ab,p)
    else:
        p=0
print(ab)
