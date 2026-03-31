# 📌 Problem: Top K Frequent Elements (LeetCode 347)
# 🎯 Goal: Return the k most frequent elements from a non-empty list of integers.

# ✅ Engineering Method:

# 1. Explore:
#    - Input: nums = [1,1,1,2,2,3], k = 2
#    - Output: [1, 2] (any order)

# 2. Brainstorm:
#    Approach 1: Use a hashmap to count frequencies, then sort based on frequency
#    Approach 2: Use a hashmap + bucket sort (frequency → elements)

# 3. Plan (Approach 1: Sorting by frequency):
#    - Count frequencies using a hashmap
#    - Convert hashmap to list of (count, number) pairs
#    - Sort this list descending by frequency
#    - Return the top k elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()  # Ascending sort by frequency

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # Grab the most frequent from end
        return res

# 4. Plan (Approach 2: Bucket Sort - O(n)):
#    - Count frequencies using hashmap
#    - Create a list of buckets where index = frequency
#    - Append numbers to corresponding bucket
#    - Iterate from highest freq to lowest until we get k elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# 5. Verify:
# Input: nums = [1,1,1,2,2,3], k = 2 → Output: [1, 2] or [2, 1]

# 6. Complexity:
# 🧠 Approach 1 (Sort-based):
#    Time: O(n log n) — due to sorting
#    Space: O(n)

# 🧠 Approach 2 (Bucket sort):
#    Time: O(n)
#    Space: O(n)

# 🔐 Edge Cases:
# - k == len(nums): should return all unique numbers
# - k == 1: should return only the most frequent element