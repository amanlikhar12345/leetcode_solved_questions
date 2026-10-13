class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # count=0
        # l=list(str(num))
        # print(l)
        # for i in l:
        #     if num%int(i)==0:
        #         count+=1
        # return count
        c=0
        for i in str(num):
            if num%int(i)==0:
                c+=1
        return c