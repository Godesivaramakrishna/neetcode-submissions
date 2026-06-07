class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sets = set(nums)
        maxs = 0
        for num in sets:
            count = 0 
            if num-1 not in sets:
                x = num 
                count = 1
                while x+1 in sets:
                    count+=1
                    x = x + 1
                maxs = max(maxs,count)
        return maxs
