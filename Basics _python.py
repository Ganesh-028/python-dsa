T = int(input())

for _ in range(T):
    X, A, B = map(int, input().split())

    score = A + (2 * B)

    if score >= X:
        print("Qualify")
    else:
        print("NotQualify")
