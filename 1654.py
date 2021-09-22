import sys
k, n = map(int, input().split())
array=[int(sys.stdin.readline()) for _ in range(k)]

start=1
end=max(array)
result=0

while start<=end:
    total=0
    mid=(start+end)//2 #랜선 길이

    for x in array:
        total += (x//mid)

    if total>=n:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)