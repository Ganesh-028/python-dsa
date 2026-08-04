class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x =[]
        p = 1
        c =0
        for i in range(len(nums)):
            if nums[i] == 0:
                c +=1
        if c==1:
            z=[]
            for i in range(len(nums)):
                if nums[i]!= 0:
                    p = p * nums[i]
            for i in range(len(nums)):
                if nums[i] == 0:
                    z.append(p)
                else:
                    z.append(0)
     
            return z
        else:
            for i in range(len(nums)):
              p = p*nums[i]
            for i in range(len(nums)):
                if nums[i] == 0:
                    x.append(p)
                else:
                    x.append(p//nums[i])
        return x
        
