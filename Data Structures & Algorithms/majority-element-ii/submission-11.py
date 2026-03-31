class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []

        # Phase 1: Find up to two candidates
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = x, 1
            elif cnt2 == 0:
                cand2, cnt2 = x, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Phase 2: Verify counts
        res = []
        n = len(nums)
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > n // 3:
                if cand not in res:      # avoid duplicates if cand1==cand2
                    res.append(cand)

        return res
