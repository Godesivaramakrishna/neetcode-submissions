class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        idx = []
        while left < right:
            sums = numbers[left]+numbers[right]
            if sums == target:
                idx.append(left+1)
                idx.append(right+1)
                left+=1
                right-=1
            elif sums < target:
                left+=1
            else:
                right-=1
        return idx