class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        maps = {0:1}
        total = 0
        count = 0
        for num in nums:
            total+=num
            remain = total - k
            if remain in maps:
                count+=maps[remain]
            maps[total] = maps.get(total,0)+1
        return count