class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i,j,k = 0,1,2
        max_idx = len(nums)
        ans = 0
        if max_idx == 3:
            ans = (nums[i] - nums[j]) * nums[k]
        


        while i <= max_idx-3:
            if k == max_idx:
                pass
            else:
                tmp = (nums[i] - nums[j]) * nums[k]
                ans = max(ans,tmp)

            if k < max_idx:
                k += 1
            else:
                if j == k-1:
                    i += 1
                    j = i + 1
                    k = j + 1
                else:
                    j += 1
                    k = j + 1
        if ans < 0:
            ans = 0
        return ans