from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        sumi=0
        s=set()
        maxi=0
        for r in range(len(nums)):
            while nums[r] in s:
                sumi-=nums[l]
                s.remove(nums[l])
                l+=1
            s.add(nums[r])
            sumi+=nums[r]

            if len(s)==k:
                maxi=max(maxi,sumi)
                sumi-=nums[l]
                s.remove(nums[l])
                l+=1
        return maxi

sol=Solution()
nums = [1, 2, 3, 4, 2, 1]
k = 3
print(sol.maximumSubarraySum(nums,k))
        