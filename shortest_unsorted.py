class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        x = sorted(nums)

        if x == nums:
            return 0

        left = 0
        right = len(nums) - 1

        while nums[left] == x[left]:
            left += 1

        while nums[right] == x[right]:
            right -= 1

        return right - left + 1
