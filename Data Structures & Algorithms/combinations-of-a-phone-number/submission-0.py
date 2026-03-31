class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []


        def helper(index,curr):

            if len(curr)==len(digits):
                res.append("".join(curr))
                return 
            

            for val in digit_to_char[digits[index]]:

                curr.append(val)
                helper(index+1,curr)
                curr.pop()
            
        helper(0,[])
        return res
