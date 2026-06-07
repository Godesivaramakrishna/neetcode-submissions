class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        a = []
        while left < right:
            b = numbers[left]+numbers[right]
            if b == target:
                a.append(left+1)
                a.append(right+1)
                break
            elif b < target:
                left+=1
            else:
                right-=1
        return a