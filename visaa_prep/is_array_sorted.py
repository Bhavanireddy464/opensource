n=int(input())
arr=list(map(int,input().split()))
arr1=sorted(arr)
if arr==arr1:
    print('true')
else:
    print('false')
