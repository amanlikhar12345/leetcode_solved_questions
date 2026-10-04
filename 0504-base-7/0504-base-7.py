class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        import numpy as np
        return str(np.base_repr(num, base=7))

        