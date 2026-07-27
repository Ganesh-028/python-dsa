t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    if sum(b) % 2 == 0:
        print("YES")
    else:
        print("NO")
