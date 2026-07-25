n = int(input())
for i in range(n):
    x =input()
    s = input()
    vowels = ["a","e","i","o","u"]
    count = 0
    maxi = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count = 0
        else:
            count += 1
            maxi = max(maxi,count)
    if maxi < 4:
        print("YES")
    else:
        print("NO")
