class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        d=set()
        for i in range(len(paths )):
            d.add(paths[i][0])
        for i in range(len(paths)):
                if paths[i][1] not in d:
                    return paths[i][1]