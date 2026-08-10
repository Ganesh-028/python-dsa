class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        x = []
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                x.append(nums[i])
        return len(x)
        
