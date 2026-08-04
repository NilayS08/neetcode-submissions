class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= n or total > target:
                return
            # include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            # skip candidates[i]
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res
