class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        for k,v in Counter(nums).items():
            if v % 2 != 0:
                return False
        return True