class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            if self.is_distinct(nums):
                return cnt
            if len(nums) < 3:
                return cnt + 1
            nums = nums[3:]
            cnt += 1

    def is_distinct(self,array: List[int]) -> bool:
        dict = defaultdict(int)
        for i in array:
            if not dict[i]:
                dict[i] = 1
            else:
                return False
        return True