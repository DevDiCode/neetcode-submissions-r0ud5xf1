class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        index1 = len(text1)
        index2 = len(text2)

        DP = [[-1 for i in range(index2)] for j in range(index1)]



        def helper(ind1,ind2):



            if ind1<0 or ind2<0:
                return 0





            if DP[ind1][ind2]!=-1:
                return DP[ind1][ind2]



            if text1[ind1] == text2[ind2]:
                DP[ind1][ind2]=  1+helper(ind1-1, ind2-1)


            else:
                skip_1 = helper(ind1-1, ind2)
                skip_2 = helper(ind1, ind2-1)

                DP[ind1][ind2] = max(skip_1, skip_2)

            return DP[ind1][ind2]


        return helper(index1-1,index2-1)
