class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s="qwertyuiopasdfghjklzxcvbnm"
        for i in s:
            if i not in sentence:
                return False
        else:
            return True