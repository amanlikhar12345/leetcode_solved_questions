class Solution:
    def greatestLetter(self, s: str) -> str:
        a=s.lower()
        r=""
        for i in a:
            if i.upper() in s and i.lower() in s:
                r+=i.upper()
        m=list(r)
        if m:
            return max(m)

        else:
            return ""