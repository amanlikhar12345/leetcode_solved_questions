class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def solve(start, total, arr):
            if total == target:
                res.append(arr[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                solve(i, total + candidates[i], arr)
                arr.pop()

        solve(0, 0, [])
        return res