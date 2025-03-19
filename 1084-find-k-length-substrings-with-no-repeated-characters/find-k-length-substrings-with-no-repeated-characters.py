class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        from collections import Counter
        max_index = len(s)
        min_index = 0
        s_list = [char for char in s]
        cnt = 0
        while min_index + k <= max_index:
            dict = Counter(s_list[min_index:min_index+k])
            tmp = 0
            for v in dict.values():
                if v != 1:
                    break
                else:
                    tmp += 1
            if tmp == k:
                cnt += 1
            min_index += 1
        return cnt