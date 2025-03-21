class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        left = right = 0
        freq = [0] * 53
        def get_val(ch: str) -> int:
            if ch.islower():
                return ord(ch) - ord('a')
            else:
                return ord(ch) - ord('A') + 27
        ans = 0
        while right < n:
            freq[get_val(s[right])] += 1
            distinct_cnt = 0
            tmp = 0
            for i in range(0,53):
                if freq[i] > 0:
                    distinct_cnt += 1
                    tmp += freq[i]
            if distinct_cnt <= 2:
                ans = max(tmp,ans)
            elif distinct_cnt > 2:
                freq[get_val(s[left])] -= 1
                left += 1
            right += 1
        return ans