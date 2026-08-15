class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        z=[]
        for i in range(len(requests)-1):
            x = abs(requests[i+1]-requests[i])
            z.append(x)
        y = sum(z) + requests[0]
        return y©leetcode
