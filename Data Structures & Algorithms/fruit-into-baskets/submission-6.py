class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        baskets = defaultdict(int)
        left = 0
        response = 0

        for right in range(len(fruits)):
            baskets[fruits[right]] += 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1

            response = max(response, right - left + 1)

        return response




        
        