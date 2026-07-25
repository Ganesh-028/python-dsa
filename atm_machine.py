n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    a = list(map(int,input().split()))
    ans = ""
    for i in range(0,x):
        if a[i] <= y:
            y -= a[i]
            ans=ans + '1'
        else:
            ans= ans + '0'
    print(ans)
