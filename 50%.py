n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    if y * 2 >= x:
        print("YES")
    else:
        print("NO")
