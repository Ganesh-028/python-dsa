from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        z = x.most_common()
        y = []

        for i in range(k):
            y.append(z[i][0])

        return y
