class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zc = 0
        l = 0
        m = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zc += 1

            while zc > k:
                if nums[l] == 0:
                    zc -= 1
                l += 1

            m = max(m, right - l + 1)

        return m
