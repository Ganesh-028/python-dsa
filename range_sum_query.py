class NumArray:
    def prefix(self, num: List[int]):
        y = []
        y.append(num[0])

        for i in range(1, len(num)):
            y.append(y[i-1] + num[i])

        return y

    def __init__(self, nums: List[int]):
        self.p = self.prefix(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.p[right]

        return self.p[right] - self.p[left - 1]
