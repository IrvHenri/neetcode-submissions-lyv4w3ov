class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        res = 0

        for r in range(len(s)):
            curr = s[r]

            while curr in window:
                window.remove(s[l])
                l +=1
            window.add(curr)
            res = max(res,r - l + 1)

        return res