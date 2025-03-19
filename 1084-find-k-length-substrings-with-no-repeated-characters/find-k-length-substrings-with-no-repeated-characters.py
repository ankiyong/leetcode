class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        max_index = len(s)
        if k == max_index:
            return 0
        min_index = 0
        s_list = [char for char in s]
        cnt = 0
        while min_index + k <= max_index:
            if len(s_list[min_index:min_index+k]) == len(set(s_list[min_index:min_index+k])):
                cnt += 1
            min_index += 1
        return cnt