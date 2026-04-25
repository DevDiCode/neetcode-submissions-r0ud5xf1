class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        print(path.split("/"))
        for val in path.split("/"):
            

            if val=="" or val ==".":
                continue
            
            elif val=="..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(val)
        

        return "/" + "/".join(stack)


        