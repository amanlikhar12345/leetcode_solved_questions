class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res=[]
        c=0
        for j in range(len(strs[0])): 
            r=[]     
            for i in range(len(strs)-1): 
                if strs[i][j] > strs[i+1][j] :
                    break
                else :
                    r.append(strs[i][j])
            res.append(r)
        
        for i in res:
            if len(i)==len(strs)-1:
                pass
            else:
                c+=1
        return c