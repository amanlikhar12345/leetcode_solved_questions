# class Solution(object):
#     def evaluate(self, s, knowledge):
#         """
#         :type s: str
#         :type knowledge: List[List[str]]
#         :rtype: str
#         """
#         if len(knowledge)==1:
#             k1="("+knowledge[0][0]
#             k2=knowledge[0][1]
        
#             print(k1,k2)

#             for i in range(len(s)):
#                 if i==k1:
#                     s[i]=k2
#                 print(s)
#             return ""+join(s)
#         else:
#             s=s.split(")")
#             print(s)
#             print()
#             k1="("+knowledge[0][0]
#             k2=knowledge[0][1]
#             k3="("+knowledge[1][0]
#             k4=knowledge[1][1]
#             print(k1,k2,k3,k4)
#             for i in range(len(s)):
#                 if i==k1:
#                     s[i]=k2
#                 if i==k3:
#                     s[i]=k4
#                 print(s)
#             return ""+join(s)
                
class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {}

        for key, value in knowledge:
            d[key] = value

        res = []
        i = 0

        while i < len(s):
            if s[i] == "(":
                j = i + 1

                while s[j] != ")":
                    j += 1

                key = s[i + 1:j]

                if key in d:
                    res.append(d[key])
                else:
                    res.append("?")

                i = j + 1
            else:
                res.append(s[i])
                i += 1

        return "".join(res)

        
            
            

        
