class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = 0
        mins = float("inf")
        l = 0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums >= target:
                mins = min(mins,r-l+1)
                sums-=nums[l]
                l+=1
        return mins if mins != float("inf") else 0