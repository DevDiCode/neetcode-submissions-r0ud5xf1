class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        response = []



        def helper(index,curr):

            if index==len(digits):
                response.append(curr)
                return 
            


            chars = digit_to_char[digits[index]]


            for val in chars:

                helper(index+1,curr+val)

        
        helper(0,"")
        return response