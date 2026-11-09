class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        else:
            return letters[0]