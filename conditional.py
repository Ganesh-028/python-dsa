t = int(input())

for _ in range(t):
    A, B, X, Y = map(int, input().split())

    if X * Y >= A * B:
        print("Yes")
    else:
        print("No")
