class Solution:
    def decodeString(self, s: str) -> str:



        string_stack = []
        count_stack = []
        digits = 0
        curr= "" 


        for val in s:

            if val.isdigit():
                
                digits = 10*digits + int(val)
                
            
            elif val =="[":
                string_stack.append(curr)
                count_stack.append(digits)
                digits = 0 
                curr = ""
            
            elif val== "]":
                temp = curr

                prev = string_stack.pop()
                count = count_stack.pop()
                curr =  prev + ( curr * count)
            
            else :
                curr+=val
        
        return curr
            
            




                
                

