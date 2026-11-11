import math
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        d={}
        for i in deck:
            d[i]=d.get(i,0)+1
        c=(math.gcd(*d.values()))
        return c>=2