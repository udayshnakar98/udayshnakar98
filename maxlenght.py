def maxlength(n,arr):
    count=0
    c=0
    for i in arr:
        if i==1:
            c+=1
        else:
            if count<c:
                count=c
            c=0
    return max(c,count)


n=int(input())
arr=list(map(int,input().split()))
print(maxlength(n,arr))
