class Solution:
    def tribonacci(self, n: int) -> int:
        to = 0
        t1 = 1
        t2 = 1
        if n < 0:
            return 0
        for i in range(n):
            curri = to+t1+t2
            to = t1
            t1 = t2
            t2 = curri
        return to