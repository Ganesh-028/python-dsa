class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        x = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                x.append(s[i])
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = x[j]
                j += 1

        return ''.join(s)
