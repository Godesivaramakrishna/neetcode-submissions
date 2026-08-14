class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch,0)+1
        ans = -1
        for key,val in freq.items():
            if val > len(nums)//2:
                ans = key
        return ans