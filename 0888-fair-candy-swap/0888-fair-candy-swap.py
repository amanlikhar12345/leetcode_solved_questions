class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        m=sum(aliceSizes)
        n=sum(bobSizes)
        res=(m-n)//2
        aliceSize=set(aliceSizes)
        for i in range(len(bobSizes)):
            x=bobSizes [i]+res
            if x in aliceSize:
                return [x,bobSizes[i]]