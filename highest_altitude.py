class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = []
        x.append(0)
        for i in range(0,len(gain)):
            x.append(x[i]+gain[i])
        return max(x)
