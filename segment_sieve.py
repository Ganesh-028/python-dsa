import math

t = int(input())

for tc in range(t):
    m, n = map(int, input().split())

    limit = int(math.sqrt(n)) + 1

    # Normal sieve up to sqrt(n)
    prime = [True] * (limit + 1)
    primes = []

    for i in range(2, limit + 1):
        if prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                prime[j] = False

    # Segmented sieve
    segment = [True] * (n - m + 1)

    for p in primes:
        start = max(p * p, ((m + p - 1) // p) * p)
        for j in range(start, n + 1, p):
            segment[j - m] = False

    if m == 1:
        segment[0] = False

    for i in range(n - m + 1):
        if segment[i]:
            print(m + i)

    if tc != t - 1:
        print()
