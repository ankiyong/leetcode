class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        ans = []

        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left += 1
            ans.append(s[right])
            max_length = max(max_length,len(ans))
        return max_length