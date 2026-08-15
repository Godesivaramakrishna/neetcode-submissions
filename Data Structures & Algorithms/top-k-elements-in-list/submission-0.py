class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        freq = [[] for i in range(len(nums)+1)]
        for ch in nums:
            maps[ch] = maps.get(ch,0)+1
        for key,val in maps.items():
            freq[val].append(key)
        res = []
        for idx in range(len(freq)-1,0,-1):
            for lists in freq[idx]:
                res.append(lists)
                if len(res) == k:
                    return res