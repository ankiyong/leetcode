class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        forward_map = defaultdict(int)
        rear_map = defaultdict(int)
        max_idx = len(nums)
        for n in nums:
            forward_map[n] += 1
        
        for i in range(max_idx):
            num = nums[i]
            forward_map[num] -= 1
            rear_map[num] += 1
            if rear_map[num] * 2 > i + 1 and forward_map[num] * 2 > max_idx - i - 1:
                return i
        return -1