class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []
        n = len(candidates)
        candidates.sort()  # optional but helps prune earlier for larger values

        def backtrack(start: int, curr_sum: int) -> None:
            if curr_sum == target:
                res.append(path.copy())
                return
            if curr_sum > target:
                return  # prune

            for i in range(start, n):
                val = candidates[i]

                if i>start and  candidates[i]== candidates[i-1]:
                    continue
                # Optional pruning: if sorted and curr_sum + val > target, break
                if curr_sum + val > target:
                    break
                path.append(val)
                # i (not i+1) because we can reuse the same candidate unlimited times
                backtrack(i+1, curr_sum + val)
                path.pop()

        backtrack(0, 0)
        return res