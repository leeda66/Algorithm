n=int(input())
array=list(map(int, input().split()))
m=int(input())

start=0
end=max(array)
result=0

while start<=end:
    total=0
    mid=(start+end)//2

    for x in array:
        if x>mid:
            total+=mid
        else:
            total+=x

    if total<=m:
        #조건 만족. 저장
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)