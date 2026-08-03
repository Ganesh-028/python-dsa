n = int(input())
for _ in range(n):
    x = int(input())
    y = x*50
    z = y*0.2 + y*0.2 + y*0.3
    print(int(y-z))
