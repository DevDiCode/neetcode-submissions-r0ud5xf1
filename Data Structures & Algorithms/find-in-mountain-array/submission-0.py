# ------------------------------------------------------
# ✅ Problem: Find in Mountain Array (Interactive)
#         (LeetCode 1095)
# ------------------------------------------------------
# Return the minimum index i such that MountainArray.get(i) == target, else -1.
# Access allowed:
#   - mountainArr.get(i)
#   - mountainArr.length()
# Constraint: ≤ 100 calls to get()
# ------------------------------------------------------

# 1) Explore:
#    - Mountain array: strictly increasing up to a peak, then strictly decreasing.
#    - Goal: smallest index with value == target.
#    - Strategy must be O(log n) to respect get() call budget.

# 2) Brainstorm:
#    - Use three binary searches (all O(log n)):
#      A) Find peak index with a slope predicate (get(mid) < get(mid+1) → go right).
#      B) Binary search ascending half [0..peak] for target (ensures minimal index if found).
#      C) If not found, binary search descending half [peak+1..n-1] with reversed comparisons.

# 3) Plan (Engineering Method):
#    - Define search spaces and monotone predicates:
#      • Peak find: while l < r:
#          m = (l+r)//2
#          if get(m) < get(m+1): l = m+1
#          else: r = m
#        Peak is l.
#      • Ascending search (lower-bound style): predicate = get(m) >= target
#        Move right = m when True; else left = m+1; post-check equality.
#      • Descending search (lower-bound style for first <= target):
#        predicate = get(m) <= target; same movement; post-check equality.

# 4) Implement:

# class MountainArray:
#     def get(self, index: int) -> int: ...
#     def length(self) -> int: ...

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # A) Find peak index using slope predicate
        def find_peak() -> int:
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2
                vm = mountainArr.get(m)
                vm1 = mountainArr.get(m + 1)
                if vm < vm1:          # still ascending → peak to the right
                    l = m + 1
                else:                 # descending or at peak → peak at/before m
                    r = m
            return l

        # B) Ascending half: lower-bound for first index with value >= target
        def search_ascending(l: int, r: int) -> int:
            while l < r:
                m = (l + r) // 2
                if mountainArr.get(m) >= target:
                    r = m
                else:
                    l = m + 1
            return l if mountainArr.get(l) == target else -1

        # C) Descending half: lower-bound for first index with value <= target
        def search_descending(l: int, r: int) -> int:
            while l < r:
                m = (l + r) // 2
                if mountainArr.get(m) <= target:
                    r = m
                else:
                    l = m + 1
            return l if mountainArr.get(l) == target else -1

        peak = find_peak()

        # Search ascending side first to ensure minimum index
        ans = search_ascending(0, peak)
        if ans != -1:
            return ans

        # Then search descending side
        return search_descending(peak + 1, n - 1)

# 5) Verify mentally:
#    - Peak found by slope predicate (monotone flip at peak).
#    - Ascending search returns minimal index if present on left.
#    - If absent on left, descending search checks right side.
#    - Total get() calls ≲ 3 * log2(n) * small constant < 100 for n ≤ 10^4.

# 6) Complexity:
#    - Time: O(log n) total
#    - Space: O(1)
