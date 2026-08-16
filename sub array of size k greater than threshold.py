class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold

        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target:
            count += 1

        for r in range(k, len(arr)):
            window_sum += arr[r]
            window_sum -= arr[r - k]

            if window_sum >= target:
                count += 1

        return count
