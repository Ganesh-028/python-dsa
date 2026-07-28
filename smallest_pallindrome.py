from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        x = Counter(s)

        left = []
        middle = ""

        for ch in sorted(x):
            left.append(ch * (x[ch] // 2))
            if x[ch] % 2 == 1:
                middle = ch

        left = "".join(left)

        return left + middle + left[::-1]
