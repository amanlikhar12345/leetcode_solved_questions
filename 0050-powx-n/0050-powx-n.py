# '''class Solution(object):
#     def myPow(self, x, n):
#         res = 1

#         if n > 0:
#             for i in range(n):
#                 res = x * res
#             return float(res)

#         elif n < 0:
#             for i in range(-n):
#                 res = x * res
#             return float(1 / res)

#         else:
#             return 1.0
# '''

# class Solution(object):
#     def myPow(self, x, n):
#         res = 1.0

#         if n < 0:
#             x = 1 / x
#             n = -n

#         while n > 0:
#             if n % 2 == 1:
#                 res = res * x

#             x = x * x
#             n = n // 2

#         return res
class Solution(object):
     def myPow(self, x, n):
        return x**n