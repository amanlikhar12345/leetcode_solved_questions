class Solution:
    def longestPrefix(self, s: str) -> str:
        o = ""
        for i in range(1,len(s)):
            prefix = s[:i]
            suffix = s[-i:]

            if prefix == suffix:
                o = prefix

        return o