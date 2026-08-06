t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    for i in range(0, n - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
    for i in range(n):
        s[i] = chr(ord('z') - (ord(s[i]) - ord('a')))

    print("".join(s))
