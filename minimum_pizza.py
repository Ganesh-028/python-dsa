n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    z = x*y
    if z % 4 == 0:
        print(z//4)
    else:
        print(z//4 +1)
