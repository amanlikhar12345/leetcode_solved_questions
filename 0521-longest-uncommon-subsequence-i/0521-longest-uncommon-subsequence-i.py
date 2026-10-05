class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
        # res=[]
        # c=0
        # for i in range(len(a)):
        #     if a[i]!=b[i]:
        #         c+=1
        #     else:
        #         if c!=0:
        #             res.append(c)
        #         c=0
        # if c!=0:
        # res.append(c)
        # print(res)
        # if len(res)>0:
        #     return max(res)
        # else:
        #     return -1
