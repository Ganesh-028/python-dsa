class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            n = i
            valid = True

            while n > 0:
                digit = n % 10

                if digit == 0 or i % digit != 0:
                    valid = False
                    break

                n //= 10

            if valid:
                ans.append(i)

        return ans
