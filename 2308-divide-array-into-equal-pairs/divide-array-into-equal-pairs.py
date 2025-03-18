class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        dict = Counter(nums)
        return all(count % 2 == 0 for count in dict.values())