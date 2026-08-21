T = int(input())

for _ in range(T):
    N = int(input())

    if N <= 15:
        deck = "Lower"
        pos = N
    else:
        deck = "Upper"
        pos = N - 15

    if pos <= 10:
        seat_type = "Double"
    else:
        seat_type = "Single"

    print(deck, seat_type)
