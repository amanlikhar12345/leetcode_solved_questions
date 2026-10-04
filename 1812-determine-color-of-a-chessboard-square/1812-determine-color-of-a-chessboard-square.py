class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        odd=[0,1,0,1,0,1,0,1,0,1]
        even=[1,0,1,0,1,0,1,0,1,0]
        d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        first=coordinates[0]
        second=int(coordinates[1])
        f=d.get(first)
        
        if f%2==0:
            return bool(even[second-1])
        else:
            return bool(odd[second-1])
